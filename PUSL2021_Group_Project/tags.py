import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=1382
        height=675
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_375=tk.Button(root)
        GButton_375["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_375["font"] = ft
        GButton_375["fg"] = "#ffffff"
        GButton_375["justify"] = "center"
        GButton_375["text"] = "Speed "
        GButton_375.place(x=100,y=190,width=257,height=101)
        GButton_375["command"] = self.GButton_375_command

        GButton_236=tk.Button(root)
        GButton_236["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_236["font"] = ft
        GButton_236["fg"] = "#ffffff"
        GButton_236["justify"] = "center"
        GButton_236["text"] = "Network Latency"
        GButton_236.place(x=100,y=320,width=257,height=104)
        GButton_236["command"] = self.GButton_236_command

        GButton_729=tk.Button(root)
        GButton_729["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_729["font"] = ft
        GButton_729["fg"] = "#ffffff"
        GButton_729["justify"] = "center"
        GButton_729["text"] = "Data Usage"
        GButton_729.place(x=100,y=450,width=253,height=94)
        GButton_729["command"] = self.GButton_729_command

        GButton_76=tk.Button(root)
        GButton_76["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_76["font"] = ft
        GButton_76["fg"] = "#ffffff"
        GButton_76["justify"] = "center"
        GButton_76["text"] = "Packet Loss"
        GButton_76.place(x=920,y=190,width=262,height=102)
        GButton_76["command"] = self.GButton_76_command

        GButton_623=tk.Button(root)
        GButton_623["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_623["font"] = ft
        GButton_623["fg"] = "#ffffff"
        GButton_623["justify"] = "center"
        GButton_623["text"] = "JItter"
        GButton_623.place(x=920,y=320,width=262,height=102)
        GButton_623["command"] = self.GButton_623_command

        GButton_408=tk.Button(root)
        GButton_408["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_408["font"] = ft
        GButton_408["fg"] = "#ffffff"
        GButton_408["justify"] = "center"
        GButton_408["text"] = "Throughput"
        GButton_408.place(x=920,y=450,width=259,height=102)
        GButton_408["command"] = self.GButton_408_command

        GMessage_873=tk.Message(root)
        GMessage_873["anchor"] = "center"
        GMessage_873["bg"] = "#01ed40"
        GMessage_873["borderwidth"] = "10px"
        ft = tkFont.Font(family='Times',size=48)
        GMessage_873["font"] = ft
        GMessage_873["fg"] = "#000000"
        GMessage_873["justify"] = "center"
        GMessage_873["text"] = "Internet Connection Checker"
        GMessage_873["relief"] = "groove"
        GMessage_873.place(x=100,y=40,width=1084,height=122)

    def GButton_375_command(self):
        print("command")


    def GButton_236_command(self):
        print("command")


    def GButton_729_command(self):
        print("command")


    def GButton_76_command(self):
        print("command")


    def GButton_623_command(self):
        print("command")


    def GButton_408_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
