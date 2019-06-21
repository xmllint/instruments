"""
Create an oscilloscope in tkinter
"""

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Scope(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Oscilloscope")
        self.geometry("800x600")
        self.resizable(width=False, height=False)
        self.fig = plt.figure(figsize=(8, 6))
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(-1, 1)
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Voltage")
        self.ax.grid()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas.draw()
        self.ani = animation.FuncAnimation(
            self.fig, self.animate, interval=100)

    def animate(self, i):
        x = np.linspace(0, 100, 100)
        y = np.sin(x + i)
        self.ax.clear()
        self.ax.plot(x, y)
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(-1, 1)
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Voltage")
        self.ax.grid()
        self.canvas.draw()


if __name__ == "__main__":
    scope = Scope()
    scope.mainloop()
