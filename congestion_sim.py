import simpy
import random
import matplotlib.pyplot as plt

QUEUE_LIMIT = 10
ARRIVAL_RATE = 1
SERVICE_RATE = 0.6
SIM_TIME = 50

queue_sizes = []

def router(env):
    queue = 0
    while True:
        queue_sizes.append(queue)

        # packet arrival
        if random.random() < ARRIVAL_RATE:
            if queue < QUEUE_LIMIT:
                queue += 1
            else:
                print(f"Dropped at time {env.now}")

        # packet departure
        if queue > 0 and random.random() < SERVICE_RATE:
            queue -= 1

        yield env.timeout(1)

env = simpy.Environment()
env.process(router(env))
env.run(until=SIM_TIME)

plt.plot(queue_sizes)
plt.title("Congestion Simulation – Queue Size Over Time")
plt.xlabel("Time (units)")
plt.ylabel("Queue Length")
plt.savefig("congestion.png")
plt.clf()

print("Congestion graph saved as congestion.png")

