# Computer Networks Simulation Project

A comprehensive computer networks simulation and visualization project that demonstrates various networking concepts including HTTP client-server communication, network topologies, packet flow, congestion control, and performance analysis.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
- [Output Files](#output-files)
- [Technical Details](#technical-details)

## 🎯 Overview

This project is designed as an educational tool for understanding computer networking concepts. It includes multiple simulation modules that demonstrate real-world networking scenarios through visualizations and interactive web interfaces.

## ✨ Features

1. **HTTP Client-Server Communication**
   - Demonstrates various HTTP status codes (2xx, 3xx, 4xx, 5xx)
   - Interactive web-based login system
   - POST and GET request handling

2. **Network Topology Visualization**
   - Star topology
   - Mesh topology
   - Ring topology
   - Custom topology designs

3. **Packet Flow Simulation**
   - Visual representation of packet routing
   - Step-by-step packet transmission
   - Network path calculation

4. **Congestion Control Simulation**
   - Queue management simulation
   - Packet dropping scenarios
   - Congestion visualization over time

5. **Performance Analysis**
   - Latency calculation
   - Throughput measurement
   - Transmission delay analysis

## 📁 Project Structure

```
cnproject/
│
├── server.py                  # HTTP server implementation
├── client.py                  # HTTP client for testing status codes
├── network_topology.py        # Client-server topology visualization
├── topology_designer.py       # Network topology generator (star, mesh, ring, custom)
├── packet_flow.py             # Packet routing simulation
├── congestion_sim.py          # Congestion control simulation
├── latency_throughput.py      # Performance analysis (latency & throughput)
├── index.html                 # Simple HTTP demo page
│
└── static/                    # Web interface files
    ├── login.html             # Login page
    ├── dashboard.html         # Dashboard page after login
    └── index.html             # Alternative index page
```

## 🔧 Requirements

### Python Packages

- `networkx` - Network graph creation and analysis
- `matplotlib` - Visualization and plotting
- `simpy` - Discrete event simulation
- `requests` - HTTP client library

### System Requirements

- Python 3.7 or higher
- TkAgg backend for matplotlib (for GUI display)

## 📦 Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd cnproject
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install required packages:**
   ```bash
   pip install networkx matplotlib simpy requests
   ```

## 🚀 Usage

### 1. HTTP Server Demo

Start the HTTP server:
```bash
python server.py
```

The server will run on `http://localhost:8080`

- Access the login page at: `http://localhost:8080/`
- Default credentials: `admin` / `123`
- Dashboard available at: `http://localhost:8080/dashboard`

### 2. HTTP Status Code Testing

In a separate terminal, run the client to test various HTTP status codes:
```bash
python client.py
```

This will demonstrate:
- 200 OK
- 301 Moved Permanently
- 302 Found (Temporary Redirect)
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 500 Internal Server Error

### 3. Network Topology Visualization

Generate topology diagrams:
```bash
python topology_designer.py
```

This creates PNG images for:
- `star_topology.png`
- `mesh_topology.png`
- `ring_topology.png`
- `custom_topology.png`

### 4. Client-Server Topology

Visualize the GET/POST request flow:
```bash
python network_topology.py
```

Displays an interactive graph showing client-server communication paths.

### 5. Packet Flow Simulation

Simulate packet routing through a network:
```bash
python packet_flow.py
```

Generates `packet_step.png` showing packet movement through routers.

### 6. Congestion Control Simulation

Run congestion simulation:
```bash
python congestion_sim.py
```

Produces `congestion.png` showing queue size over time.

### 7. Latency and Throughput Analysis

Analyze network performance:
```bash
python latency_throughput.py
```

Generates `latency.png` and calculates throughput metrics.

## 📊 Components

### Server (`server.py`)
- Custom HTTP server implementation
- Handles GET and POST requests
- Implements various HTTP status codes
- Serves static HTML files
- JSON response handling for API endpoints

### Client (`client.py`)
- Tests HTTP server with various request types
- Demonstrates status code handling
- Shows redirection behavior

### Network Topology (`network_topology.py`)
- Creates directed graph of client-server interaction
- Visualizes GET and POST request flows
- Shows server-side processing paths

### Topology Designer (`topology_designer.py`)
- Generates multiple network topologies
- Supports configurable node counts
- Saves topology diagrams as PNG files

### Packet Flow (`packet_flow.py`)
- Simulates packet transmission
- Shows hop-by-hop routing
- Visualizes shortest path algorithms

### Congestion Simulation (`congestion_sim.py`)
- Discrete event simulation of network congestion
- Queue management with packet dropping
- Configurable arrival and service rates

### Latency Throughput (`latency_throughput.py`)
- Calculates transmission, propagation, and processing delays
- Measures network throughput
- Generates latency graphs

## 📸 Output Files

The following files are generated when running simulations:

- `star_topology.png` - Star network topology diagram
- `mesh_topology.png` - Mesh network topology diagram
- `ring_topology.png` - Ring network topology diagram
- `custom_topology.png` - Custom network topology diagram
- `packet_step.png` - Packet routing visualization
- `congestion.png` - Congestion queue size graph
- `latency.png` - Packet latency graph

## 🔬 Technical Details

### HTTP Status Codes Demonstrated

| Code | Name | Usage |
|------|------|-------|
| 200 | OK | Successful request |
| 301 | Moved Permanently | Permanent redirect |
| 302 | Found | Temporary redirect |
| 400 | Bad Request | Invalid client request |
| 401 | Unauthorized | Authentication required |
| 403 | Forbidden | Access denied |
| 404 | Not Found | Resource not found |
| 500 | Internal Server Error | Server error |

### Network Topologies

- **Star**: Central hub with connected nodes (N connections)
- **Mesh**: Fully connected network (N(N-1)/2 connections)
- **Ring**: Circular connection pattern (N connections)
- **Custom**: User-defined network structure

### Simulation Parameters

**Congestion Simulation:**
- Queue limit: 10 packets
- Arrival rate: 1 packet/time unit
- Service rate: 0.6 packets/time unit
- Simulation time: 50 time units

**Latency/Throughput Analysis:**
- Bandwidth: 5 Mbps
- Packet size: 1 MB
- Propagation delay: 20 ms
- Processing delay: 5 ms
- Packet count: 20 packets

## 🎓 Educational Value

This project is ideal for:
- Learning HTTP protocol fundamentals
- Understanding network topologies
- Studying packet routing algorithms
- Analyzing network performance metrics
- Practicing discrete event simulation

## 📝 Notes

- The server uses Python's built-in `http.server` module
- Network visualizations use NetworkX and Matplotlib
- Simulations use SimPy for event-driven modeling
- All topology images are saved in the project root directory

## 👨‍💻 Development

To modify or extend this project:
1. Adjust simulation parameters in the respective Python files
2. Modify topology designs in `topology_designer.py`
3. Customize web interface in `static/` directory
4. Extend HTTP server functionality in `server.py`

## 📄 License

This project is created for educational purposes as part of a Computer Networks course.

## 🙏 Acknowledgments

- NetworkX for graph manipulation
- Matplotlib for visualizations
- SimPy for discrete event simulation

---

**Project for Semester 5 - Computer Networks Course**

