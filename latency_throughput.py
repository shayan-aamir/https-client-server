import simpy
import random
import matplotlib.pyplot as plt

RANDOM_SEED = 40
PACKET_COUNT = 20
BANDWIDTH = 5e6        # 5 Mbps
PACKET_SIZE = 1e6      # 1 MB
PROP_DELAY = 20        # ms
PROCESSING_DELAY = 5   # ms

latencies = []
times = []

def packet(env, name):
    start = env.now
    
    # Transmission delay
    tx_delay = (PACKET_SIZE / BANDWIDTH) * 1000
    
    total_delay = tx_delay + PROP_DELAY + PROCESSING_DELAY
    yield env.timeout(total_delay)
    
    latencies.append(total_delay)
    times.append(env.now)

    print(f"{name} delivered in {total_delay:.2f} ms")

def run_sim(env):
    for i in range(PACKET_COUNT):
        env.process(packet(env, f"Packet_{i+1}"))
        yield env.timeout(random.randint(1, 5))  # Space out packets

# ------------------------------- MAIN ----------------------------------

random.seed(RANDOM_SEED)
env = simpy.Environment()

env.process(run_sim(env))
env.run()

# Safety check — if times is empty, force value to avoid crash
if not times:
    times = [1]

# Latency plot
plt.plot(latencies, marker="o")
plt.title("Packet Latency (ms)")
plt.xlabel("Packet Number")
plt.ylabel("Latency (ms)")
plt.savefig("latency.png")
plt.clf()

# Throughput calculation
total_data = PACKET_COUNT * PACKET_SIZE
total_time = max(times)

throughput = total_data / total_time

print(f"\nAverage Throughput: {throughput/1e6:.2f} MB/s")
print("Graph saved as latency.png")

