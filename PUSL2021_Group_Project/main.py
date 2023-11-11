from tkinter import *
import psutil
import time
import matplotlib.pyplot as plt
import time
import ping3
import matplotlib.pyplot as plt
from collections import deque
from tkinter import *
import psutil
import time
import matplotlib.pyplot as plt
from ping3 import ping, verbose_ping
from collections import deque
import random
from matplotlib.animation import FuncAnimation
from tkinter import *
import psutil
import time
import matplotlib.pyplot as plt
from ping3 import ping, verbose_ping
from collections import deque
import random
from matplotlib.animation import FuncAnimation
from tkinter import ttk

# ------------------Speed test ----------------------------------------------------
total_speeds = []

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

# --------------------------latency function--------------------------
destination_address = "8.8.8.8"
ping_interval = 1
timestamps = []
latency_values = []
def get_latency():
    plt.ion()  
    fig, ax = plt.subplots()
    plt.xlabel("Time (s)")
    plt.ylabel("Latency (ms)")
    plt.title("Ping Latency vs. Time")
    line, = ax.plot(timestamps, latency_values)
    max_data_points = 30  # Adjust as needed
    data_buffer = deque(maxlen=max_data_points)
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
time_intervals = []
packet_loss = []

def update_data(i):
    time_intervals.append(i)
    packet_loss.append(random.uniform(0, 5))  # Simulated packet loss in percentage

    plt.cla()
    plt.plot(time_intervals, packet_loss, color='blue', marker='o', linestyle='-', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Packet Loss (%)')
    plt.title('Network Packet Loss Over Time')
    plt.grid(True)

def check_packet_loss():
    ani = FuncAnimation(plt.gcf(), update_data, interval=1000)  # 1,000 milliseconds (1 second)
    plt.show()
# -------------------------------packet loss -------------------------------
time_intervals = []
packet_loss = []

def update_data(i):
    time_intervals.append(i)
    packet_loss.append(random.uniform(0, 5))  # Simulated packet loss in percentage

    plt.cla()
    plt.plot(time_intervals, packet_loss, color='blue', marker='o', linestyle='-', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Packet Loss (%)')
    plt.title('Network Packet Loss Over Time')
    plt.grid(True)

def check_packet_loss():
    ani = FuncAnimation(plt.gcf(), update_data, interval=1000)  # 1,000 milliseconds (1 second)
    plt.show()
# ------------------------data Usage----------------------------------------
def get_data_usage():
    net_stats = psutil.net_io_counters()
    uploaded = net_stats.bytes_sent
    downloaded = net_stats.bytes_recv
    return uploaded, downloaded

def update_table():
    uploaded_start, downloaded_start = get_data_usage()
    time.sleep(10)
    uploaded_end, downloaded_end = get_data_usage()   
    uploaded_diff = uploaded_end - uploaded_start
    downloaded_diff = downloaded_end - downloaded_start
    
    uploaded_mb = uploaded_diff / (1024 * 1024)  
    downloaded_mb = downloaded_diff / (1024 * 1024)    
    count = len(tree.get_children()) + 1
    tree.insert("", "end", values=(f"Count {count}", f"{uploaded_mb:.2f} MB", f"{downloaded_mb:.2f} MB"))   
    window.after(10000, update_table)

# ---------------------------------jitter----------------------------------------------------
time_intervals = []
jitter_values = []

def update_data(i):
    time_intervals.append(i)
    jitter_values.append(np.random.uniform(0, 5))  # Simulated jitter

    while time_intervals and time_intervals[0] < i - 10:
        time_intervals.pop(0)
        jitter_values.pop(0)

    plt.cla()
    plt.plot(time_intervals, jitter_values, color='red', marker='o', linestyle='-', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Jitter')
    plt.title('Network Jitter Over Time')
    plt.grid(True)

def check_jitter():
    ani = FuncAnimation(plt.gcf(), update_data, interval=1000)  # 1,000 milliseconds (1 second)
    plt.show()
# ---------------------------UI-----------------------------

window = Tk()
window.title("Group project")
window.geometry('900x800')

speed_test_button = Button(text = "Speed test" , padx= 20 , pady=20 , command=  measure_network_speed)
network_latecncy = Button(text = "Network latecy test", padx= 20 , pady=20,command = get_latency)
data_usage = Button(text = "Data usage", padx= 20 , pady=20, command = update_table)
packet_loss = Button(text = "Packets loss", padx= 20 , pady=20 , command = check_packet_loss)
jitter = Button(text = "Jitter", padx= 20 , pady=20 ,  command = check_jitter) 
thoughput = Button(text = "Throughput", padx= 20 , pady=20)

speed_test_button.grid(column= 1 , row = 4)
network_latecncy.grid(column = 1 , row = 5)
data_usage.grid(column = 1 , row =6)

packet_loss.grid(column = 3 , row =  4)
jitter.grid(column = 3 , row =5)
thoughput.grid(column = 3 , row =6)

window.mainloop()
