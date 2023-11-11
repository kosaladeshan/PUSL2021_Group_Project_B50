import time
import ping3
import matplotlib.pyplot as plt
from collections import deque

# Specify the destination address (e.g., an IP address or a hostname)
destination_address = "8.8.8.8"  # Example: Google's DNS server

# Define the time interval between pings (in seconds)
ping_interval = 1  # Adjust this as needed

# Initialize lists to store timestamp and latency data
timestamps = []
latency_values = []

# Set up the plot
plt.ion()  # Turn on interactive mode for real-time plotting
fig, ax = plt.subplots()
plt.xlabel("Time (s)")
plt.ylabel("Latency (ms)")
plt.title("Ping Latency vs. Time")
line, = ax.plot(timestamps, latency_values)

# Create a deque to limit the number of data points displayed
max_data_points = 30  # Adjust as needed
data_buffer = deque(maxlen=max_data_points)

# Ping loop
while True:
    # Call the ping() function with the destination address
    response_time = ping3.ping(destination_address)

    # Check if the ping was successful
    if response_time is not None:
        timestamps.append(time.time())
        latency_values.append(response_time)
        data_buffer.append((time.time(), response_time))

        # Update the plot data
        line.set_xdata(timestamps)
        line.set_ydata(latency_values)

        # Adjust the plot's x-axis limits based on the data
        ax.relim()
        ax.autoscale_view()

        # Redraw the plot
        plt.draw()
        plt.pause(0.1)  # Adjust the pause time as needed

    # Wait for the specified interval before the next ping
    time.sleep(ping_interval)

# This code will run indefinitely until manually stopped.
