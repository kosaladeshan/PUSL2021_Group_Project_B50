import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Initialize empty lists for time intervals and jitter
time_intervals = []
jitter_values = []

# Create a function to update data
def update_data(i):
    # Simulate collecting real-time jitter data (replace this with your data collection logic)
    # In this example, we generate random jitter values.
    time_intervals.append(i)
    jitter_values.append(np.random.uniform(0, 5))  # Simulated jitter

    # Remove data older than 10 seconds
    while time_intervals and time_intervals[0] < i - 10:
        time_intervals.pop(0)
        jitter_values.pop(0)

    # Update the graph with the new data
    plt.cla()
    plt.plot(time_intervals, jitter_values, color='red', marker='o', linestyle='-', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Jitter')
    plt.title('Network Jitter Over Time')
    plt.grid(True)

# Create a FuncAnimation to update the graph every 10 seconds
ani = FuncAnimation(plt.gcf(), update_data, interval=1000)  # 10,000 milliseconds (10 seconds)

# Show the graph
plt.show()
