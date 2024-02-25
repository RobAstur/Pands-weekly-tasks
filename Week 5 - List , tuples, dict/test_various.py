# This is my program that outputs whether or not today is a weekday
# Author : Roberto Gomez Garcia

import random

week   = [
              'Monday', 
              'Tuesday', 
              'Wednesday', 
              'Thursday',  
              'Friday', 
              'Saturday',
              'Sunday']
i = ""
'''
for i in week:
    i = random.choice(week)
    if i == "Sunday" or i == "Saturday":
        print(i, "It is the weekend, yay!")
    else:
        print(i , "Yes, unfortunately today is a weekday.")
'''
'''
for i in week:
    if i == "Sunday" or i == "Saturday":
        print(i, "It is the weekend, yay!")
    else:
        print(i , "Yes, unfortunately today is a weekday.")
'''

for i in week:
    print(f"please choose any value in the list: ", week)
    print("To close the loop please type quit")
    while i != "quit":
        i = str(input("input a day of the week, to finalize write x"))
        if i is not week:
            i =input("please select item from the list")
        if i =="Saturday" or i == "Sunday":
            print("It is the weekend, yay!")
        else:
            print("Yes, unfortunately today is a weekday.")
    
    


    

