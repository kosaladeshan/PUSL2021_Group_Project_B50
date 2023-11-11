import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Initialize empty lists for time intervals and packet loss
time_intervals = []
packet_loss = []

# Create a function to update data
def update_data(i):
    # Simulate collecting real-time data (replace this with your data collection logic)
    # In this example, we generate random packet loss values.
    time_intervals.append(i)
    packet_loss.append(random.uniform(0, 5))  # Simulated packet loss in percentage

    # Update the graph with the new data
    plt.cla()
    plt.plot(time_intervals, packet_loss, color='blue', marker='o', linestyle='-', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Packet Loss (%)')
    plt.title('Network Packet Loss Over Time')
    plt.grid(True)

# Create a FuncAnimation to update the graph every 10 seconds
ani = FuncAnimation(plt.gcf(), update_data, interval=1000)  # 10,000 milliseconds (10 seconds)

# Show the graph
plt.show()
