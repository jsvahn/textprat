import tkinter as tk
import subprocess
from tkinter import font

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.active_talk_sp = None

    def create_widgets(self):
        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")

        big_text_font = font.Font(family='Helvetica', name='bigTextFont', size=48, weight='bold')


        self.text_input = tk.StringVar()
        self.text_input.trace_add("write", self.text_changed)
        self.text_box = tk.Entry(self, textvariable=self.text_input, font=big_text_font)
        self.text_box.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def text_changed(self, *args):        
        if not self.active_talk_sp is None:
            print(self.active_talk_sp.poll())
            if self.active_talk_sp.poll() is None:
                self.active_talk_sp.terminate()
        self.active_talk_sp = subprocess.Popen(["say", "-v", "Alva", self.text_input.get()])
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()
