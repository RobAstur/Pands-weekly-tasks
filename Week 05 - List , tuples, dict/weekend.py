# This is my program that outputs whether or not today is a weekday
# Author : Roberto Gomez Garcia
# I got the idesa for this program from https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python#:~:text=import%20datetime%20today%20%3D%20datetime.,4%3A%20print(%22Hooray!
# Week days has allocated numbers form 0 to 6. 0 to 4 = monday t Friday. 5 and 6 are the weekend days. 
# I left today funtion in the print and it gives today days, hour and another number (not sure what it is). That could be removed but I think it is good to have it there, It shows that it is working.
#Last note: I wrote below on weekend so I will need to double check during week days if it works :)


import datetime

today = datetime.datetime.today()

if today.weekday() == 5 or today.weekday() == 6:
    print(f" {today}, It is the weekend, yay!")
else:
    print(f" {today}, Yes, unfortunately today is a weekday.")
    
