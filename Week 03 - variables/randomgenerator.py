import random
number = random.randint(1,10)
guess = int(input("Guess the number "))
print("here is teh random number", (number))
print ("here is your guess ", guess)
if number == guess:
    print ("That's correct")
else:
    print ("no correct")