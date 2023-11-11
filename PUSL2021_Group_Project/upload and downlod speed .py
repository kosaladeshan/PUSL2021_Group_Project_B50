import psutil
import time
import matplotlib.pyplot as plt

# Declare total_speeds as a global variable
total_speeds = []

# Function to measure network speed
def measure_network_speed(interval=1):
    last_time = time.time()
    last_bytes_sent = psutil.net_io_counters().bytes_sent
    last_bytes_recv = psutil.net_io_counters().bytes_recv

    download_speeds = []
    upload_speeds = []
    time_points = []

    while True:
        time_elapsed = time.time() - last_time
        current_bytes_sent = psutil.net_io_counters().bytes_sent
        current_bytes_recv = psutil.net_io_counters().bytes_recv

        upload_speed = ((current_bytes_sent - last_bytes_sent) / time_elapsed) / 1_000_000  # Convert to Mbps
        download_speed = ((current_bytes_recv - last_bytes_recv) / time_elapsed) / 1_000_000  # Convert to Mbps
        total_speed = ((upload_speed + download_speed) / time_elapsed) / 1_000_000  # Convert to Mbps

        last_time = time.time()
        last_bytes_sent = current_bytes_sent
        last_bytes_recv = current_bytes_recv

        download_speeds.append(download_speed)
        upload_speeds.append(upload_speed)
        total_speeds.append(total_speed)
        time_points.append(last_time)

        if len(download_speeds) > 60:  # Keep the last 60 data points (adjust as needed)
            download_speeds.pop(0)
            upload_speeds.pop(0)
            total_speeds.pop(0)
            time_points.pop(0)

        update_plot(download_speeds, upload_speeds, time_points, total_speeds)
        time.sleep(interval)

# Function to update the Matplotlib plot
def update_plot(download_speeds, upload_speeds, time_points, total_speeds):
    plt.clf()
    plt.plot(time_points, download_speeds, label='Download Speed (Mbps)', marker='o',color = "green")
    plt.plot(time_points, upload_speeds, label='Upload Speed (Mbps)', marker='o', color = "blue")
    plt.plot(time_points, total_speeds, label='Total Speed (Mbps)', marker='o',color = "red")
    plt.xlabel('Time')
    plt.ylabel('Speed (Mbps)')
    plt.title('Real-time Network Speed Monitor')
    plt.legend()
    plt.grid()
    plt.pause(0.01)

# Main function
def main():
    plt.ion()  # Turn on interactive mode for Matplotlib
    measure_network_speed()

if __name__ == "__main__":
    main()
