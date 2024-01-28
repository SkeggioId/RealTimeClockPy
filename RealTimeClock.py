import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time)
    window.after(1000, update_time)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")

# Create a label to display the time
time_label = tk.Label(window, font=('Arial', 50), fg='blue')
time_label.pack()

# Update the time every second
update_time()

# Run the application
window.mainloop()
