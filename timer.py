import tkinter as tk
from tkinter import ttk

class CountdownTimer(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("COUNTDOWN TIMER")
        self.geometry("400x300")
        self.resizable(False, False)
        self.configure(background="red")
        self.countdown_time = tk.StringVar()
        self.countdown_time.set("00:00:00")
        self.remaining_time = 0
        self.countdown_running = False
        self.time_frame = ttk.Frame(self)
        self.time_frame.pack(padx=10, pady=10)
        self.time_label = ttk.Label(self.time_frame, textvariable=self.countdown_time, font=("Helvetica", 40))
        self.time_label.pack()
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(padx=10, pady=10)
        self.start_button = ttk.Button(self.button_frame, text="START", command=self.start)
        self.start_button.grid(row=0, column=0, padx=5, pady=5)
        self.start_button = ttk.Button(self.button_frame, text="RESUME", command=self.resume)
        self.start_button.grid(row=0, column=2, padx=5, pady=5)
        self.stop_button = ttk.Button(self.button_frame, text="PAUSE", command=self.stop)
        self.stop_button.grid(row=0, column=1, padx=5, pady=5)
        self.reset_button = ttk.Button(self.button_frame, text="RESET", command=self.reset)
        self.reset_button.grid(row=0, column=3, padx=5, pady=5)
        self.entry_frame = ttk.Frame(self)
        self.entry_frame.pack(padx=10, pady=10)
        self.entry_label = ttk.Label(self.entry_frame, text="Enter Time in Seconds:")
        self.entry_label.grid(row=0, column=0, padx=5, pady=5)
        self.entry_box = ttk.Entry(self.entry_frame, width=10)
        self.entry_box.grid(row=0, column=1, padx=5, pady=5)
        self.set_button = ttk.Button(self.entry_frame, text="Set", command=self.set)
        self.set_button.grid(row=0, column=2, padx=5, pady=5)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def start(self):
        if self.countdown_running:
            return
        self.countdown_running = True
        self.perform_countdown()
        
    def resume(self):
        if self.countdown_running:
            return
        self.countdown_running = True
        self.perform_countdown()

    def stop(self):
        self.countdown_running = False

    def reset(self):
        self.stop()
        self.remaining_time = 0
        self.countdown_time.set("00:00:00")

    def set(self):
        self.remaining_time = int(self.entry_box.get())

    def perform_countdown(self):
        if self.remaining_time <= 0:
            self.reset()
            return
        if not self.countdown_running:
            return
        m, s = divmod(self.remaining_time, 60)
        h, m = divmod(m, 60)
        self.countdown_time.set("{:02d}:{:02d}:{:02d}".format(h, m, s))
        self.remaining_time = self.remaining_time - 1
        self.after(1000, self.perform_countdown)

    def on_closing(self):
        self.destroy()

if _name_ == "_main_":
    app = CountdownTimer()
    app.mainloop()
