import tkinter as tk
import math
import time

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock")

        # Create canvas to draw the clock
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Draw clock face
        self.clock_face = self.canvas.create_oval(50, 50, 350, 350, outline="black", width=2)

        # Draw clock hands
        self.hour_hand = self.canvas.create_line(200, 200, 200, 120, width=4, fill="black")
        self.minute_hand = self.canvas.create_line(200, 200, 200, 100, width=3, fill="black")
        self.second_hand = self.canvas.create_line(200, 200, 200, 90, width=2, fill="red")

        # Update clock every 1000ms (1 second)
        self.update_clock()

    def update_clock(self):
        # Get current time
        current_time = time.localtime()
        hours = current_time.tm_hour % 12  # Convert to 12-hour format
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # Calculate angles for each hand
        hour_angle = math.radians((hours * 30) + (minutes * 0.5) - 90)
        minute_angle = math.radians((minutes * 6) - 90)
        second_angle = math.radians((seconds * 6) - 90)

        # Update hands' positions
        self.canvas.coords(self.hour_hand, 200, 200, 200 + 60 * math.cos(hour_angle), 200 + 60 * math.sin(hour_angle))
        self.canvas.coords(self.minute_hand, 200, 200, 200 + 80 * math.cos(minute_angle), 200 + 80 * math.sin(minute_angle))
        self.canvas.coords(self.second_hand, 200, 200, 200 + 90 * math.cos(second_angle), 200 + 90 * math.sin(second_angle))

        # Update every second
        self.root.after(1000, self.update_clock)

def main():
    root = tk.Tk()
    analog_clock = AnalogClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
