#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
#create a function called <tt>sqrt</tt>
#As reference I used your video function syntax. 
#Author: roberto Gomez Garcia 

def square_root(numbers, raiz_cuadrada = 0.5):
    return (numbers ** raiz_cuadrada)

num = float(input("add a positive float "))
print(f"Square root of {num}, is {square_root(num)}")
