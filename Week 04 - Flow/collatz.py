#The Collatz conjecture is one of the most famous unsolved problems in mathematics. The conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1.
#This program represents the collatz
#Author: Roberto Gomez Garcia


initial_number = int(input("please enter a positive integer"))

while initial_number != 1:
    if initial_number%2 ==0:
        initial_number = initial_number // 2
        print(initial_number)
    else:
        initial_number = initial_number*3+1
        print(initial_number)
else:
    print(f"We have reached {initial_number} the program has ended")



   

    

