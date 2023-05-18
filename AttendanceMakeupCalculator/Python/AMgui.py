import datetime
import math
import sys
import tkinter as tk

def calculate():
    total_hours_possible = float(total_hours_possible_entry.get())
    percent_goal = float(percent_goal_entry.get())
    hours_absent = float(hours_absent_entry.get())
    hours_makeup = float(hours_makeup_entry.get())
    uo_minutes = float(uo_minutes_entry.get())
    
    uo_hours = uo_minutes / 60
    total_hours_missed = hours_absent - hours_makeup
    percent_decimal = percent_goal / 100
    uo_total = total_hours_missed - uo_hours
    current_hours = total_hours_possible - total_hours_missed
    current_decimal = current_hours / total_hours_possible
    current_percent = current_decimal * 100
    possible_absent_hours = total_hours_possible * percent_decimal
    max_absent_hours = total_hours_possible - possible_absent_hours
    hours_needed = total_hours_missed - max_absent_hours - uo_hours
    time = hours_needed
    hours = int(time)
    minutes = (time * 60) % 60
    seconds = (time * 3600) % 60
    rounded = round(hours_needed, 2)
    percent_rounded = round(current_percent, 2)
    
    result_text = ""
    
    if current_percent < percent_goal:
        result_text = "With your goal of {}%, you still need to make up {:.2f} hours as a decimal, or {} hours and {:02d} minutes.".format(
            percent_goal, rounded, hours, int(minutes)
        )
    elif current_percent > percent_goal:
        result_text = "Your current percent is {}. You do not need to make up any more time.".format(percent_rounded)
    
    result_text_widget.delete(1.0, tk.END)
    result_text_widget.insert(tk.END, result_text + "\n\nCheck the text file Hours_to_makeup.txt for a copy!")
    
    # Print to console
    print(result_text)
    
    # Print to file
    with open('Hours_to_makeup.txt', 'w') as f:
        print(result_text, file=f)

# Create the main window
window = tk.Tk()
window.title("Attendance Calculator")

# Create input labels and entry fields
total_hours_possible_label = tk.Label(window, text="How many hours are possible in the course?")
total_hours_possible_label.pack()
total_hours_possible_entry = tk.Entry(window)
total_hours_possible_entry.pack()

percent_goal_label = tk.Label(window, text="What is your goal percentage for attendance?")
percent_goal_label.pack()
percent_goal_entry = tk.Entry(window)
percent_goal_entry.pack()

hours_absent_label = tk.Label(window, text="How many hours were you absent?")
hours_absent_label.pack()
hours_absent_entry = tk.Entry(window)
hours_absent_entry.pack()

hours_makeup_label = tk.Label(window, text="How many hours have you officially made up?")
hours_makeup_label.pack()
hours_makeup_entry = tk.Entry(window)
hours_makeup_entry.pack()

uo_minutes_label = tk.Label(window, text="Have you made up any hours unofficially? (in minutes)")
uo_minutes_label.pack()
uo_minutes_entry = tk.Entry(window)
uo_minutes_entry.pack()

# Create calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Create result text widget
result_text_widget = tk.Text(window, height=6, width=40)
result_text_widget.pack()

# Start the GUI event loop
window.mainloop()
