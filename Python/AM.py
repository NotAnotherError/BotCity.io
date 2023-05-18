import math
import datetime
import sys

#information Collection
total_hours_possible = float(input("How many hours are possible in the course?: "))
percent_goal = float(input("What is your goal percentage for attendance?: "))
hours_absent = float(input("How many hours were you absent?: "))
hours_makeup = float(input("How many hours have you officially made up?: "))
uo_minutes = float(input("Have you made up any hours unofficially? (in minutes): "))

#get the hours into decimal format
uo_hours = uo_minutes / 60

#getting the hours that still need to be made up and some conversions
total_hours_missed = hours_absent - hours_makeup
percent_decimal = percent_goal / 100
uo_total = total_hours_missed - uo_hours

#Conversions
current_hours = total_hours_possible - total_hours_missed
current_decimal = current_hours / total_hours_possible
current_percent = current_decimal * 100

#Final Maths
possible_absent_hours = total_hours_possible * percent_decimal
max_absent_hours = total_hours_possible - possible_absent_hours
hours_needed = total_hours_missed - max_absent_hours - uo_hours
    
#convert the hours needed back from decimal to hours and minutes, and formatting
time = hours_needed
hours = int(time)
minutes = (time*60) % 60
seconds = (time*3600) % 60

rounded = round(hours_needed, 2)
percent_rounded = round(current_percent, 2)

if current_percent < percent_goal :
    goals_not_met = print("With your goal of" ,percent_goal,"% you still need to make up" ,rounded,"hours as a decimal, or ""%d hours and %02d minutes." % (hours, minutes,))
elif current_percent > percent_goal :
    goals_met = print("Your current percent is",percent_rounded,". So you do not need to make up any more time.")

#print to console    
print('Check the text file Hours_to_makeup for a copy!')

#print to file
with open('Hours_to_makeup', 'w') as f:
    if current_percent < percent_goal :
        print("With your goal of" ,percent_goal,"% you are at ",percent_rounded,"% you still need to make up" ,rounded,"hours as a decimal, or ""%d hours and %02d minutes." % (hours, minutes,), file=f)
    elif current_percent > percent_goal :
        print("Your current percent is",percent_rounded,". So you do not need to make up any more time.",file=f)
