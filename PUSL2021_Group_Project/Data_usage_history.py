import psutil
import time
import tkinter as tk
from tkinter import ttk

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
    root.after(10000, update_table)
root = tk.Tk()
root.title("Network Data Usage")


tree = ttk.Treeview(root, columns=("Count", "Uploaded", "Downloaded"))
tree.heading("#1", text="Count")
tree.heading("#2", text="Uploaded")
tree.heading("#3", text="Downloaded")
tree.pack()


update_table()

root.mainloop()
