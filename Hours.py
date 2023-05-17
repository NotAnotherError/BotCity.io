import math

total_hours=int(float('How many hours total are there in the course?'))
percent_needed=float(int('What is the percent needed to graduate?'))
hours_missed=float(int('How many hours have you missed?'))
hours_made_up=float(int('How many hours have been officially made up?'))
hours_made=float(int('How many hours have you made up unofficially?'))

decimal = percent_needed / 100
hours_for_percent = total_hours * decimal
diff = total_hours - hours_for_percent
hours_to_make_up_O = hours_missed - hours_made_up
hours_UO = hours_to_make_up_O - hours_made 
days_missed = hours_missed / 3
current_percent = ((total_hours - hours_to_make_up_O) / total_hours) * 100

print('You need ' + percent_needed + 'of' + total_hours + 'in order to graduate. You have missed ' + hours_missed + 'which has you at ' + current_percent)