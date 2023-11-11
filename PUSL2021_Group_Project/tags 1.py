import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=1312
        height=683
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_375=tk.Button(root)
        GButton_375["bg"] = "#19e4d0"
        GButton_375["borderwidth"] = "10px"
        ft = tkFont.Font(family='Times',size=28)
        GButton_375["font"] = ft
        GButton_375["fg"] = "#ffffff"
        GButton_375["justify"] = "center"
        GButton_375["text"] = "Speed "
        GButton_375["relief"] = "raised"
        GButton_375.place(x=100,y=190,width=360,height=98)
        GButton_375["command"] = self.GButton_375_command

        GButton_236=tk.Button(root)
        GButton_236["bg"] = "#19e4d0"
        GButton_236["borderwidth"] = "10px"
        ft = tkFont.Font(family='Times',size=28)
        GButton_236["font"] = ft
        GButton_236["fg"] = "#ffffff"
        GButton_236["justify"] = "center"
        GButton_236["text"] = "Network Latency"
        GButton_236.place(x=100,y=320,width=357,height=92)
        GButton_236["command"] = self.GButton_236_command

        GButton_729=tk.Button(root)
        GButton_729["bg"] = "#19e4d0"
        GButton_729["borderwidth"] = "10px"
        ft = tkFont.Font(family='Times',size=28)
        GButton_729["font"] = ft
        GButton_729["fg"] = "#ffffff"
        GButton_729["justify"] = "center"
        GButton_729["text"] = "Data Usage"
        GButton_729.place(x=100,y=450,width=359,height=88)
        GButton_729["command"] = self.GButton_729_command

        GButton_76=tk.Button(root)
        GButton_76["bg"] = "#19e4d0"
        GButton_76["borderwidth"] = "10px"
        ft = tkFont.Font(family='Times',size=28)
        GButton_76["font"] = ft
        GButton_76["fg"] = "#ffffff"
        GButton_76["justify"] = "center"
        GButton_76["text"] = "Packet Loss"
        GButton_76.place(x=820,y=190,width=363,height=96)
        GButton_76["command"] = self.GButton_76_command

        GButton_623=tk.Button(root)
        GButton_623["bg"] = "#19e4d0"
        GButton_623["borderwidth"] = "10px"
        ft = tkFont.Font(family='Times',size=28)
        GButton_623["font"] = ft
        GButton_623["fg"] = "#ffffff"
        GButton_623["justify"] = "center"
        GButton_623["text"] = "JItter"
        GButton_623.place(x=820,y=320,width=364,height=86)
        GButton_623["command"] = self.GButton_623_command

        GButton_408=tk.Button(root)
        GButton_408["bg"] = "#19e4d0"
        GButton_408["borderwidth"] = "10px"
        ft = tkFont.Font(family='Times',size=28)
        GButton_408["font"] = ft
        GButton_408["fg"] = "#ffffff"
        GButton_408["justify"] = "center"
        GButton_408["text"] = "Throughput"
        GButton_408.place(x=820,y=440,width=367,height=86)
        GButton_408["command"] = self.GButton_408_command

        GMessage_873=tk.Message(root)
        GMessage_873["bg"] = "#30ed01"
        GMessage_873["borderwidth"] = "10px"
        ft = tkFont.Font(family='Arial',size=18)
        
        GMessage_873["font"] = ft
        GMessage_873["fg"] = "#000000"
        GMessage_873["text"] = "Internet Connection Checker"
        GMessage_873["justify"] = "center"
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
