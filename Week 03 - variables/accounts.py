#Exercise number 2: Account.py
#Author: Roberto Gomez Garcia
#Part 1: Create a program and print only the last four digits of a 10 digits number, replacing the first 6 by X

bank_account = "10"

while len(bank_account) != 10:
    bank_account = input("PLease add the 10 digits account ")
    if len(bank_account) != 10:
        print ("Error")
else:
    print("Perfect, the bank account is: ","XXXXXX"+bank_account[:4])
  



#Part 2: I couldnt find a solution by my own on this one but I found below in internet that works perfectly.
# https://stackoverflow.com/questions/40842451/how-do-i-use-the-replace-function-to-change-all-but-the-last-4-characters-of


bank_account = input("Input your bank account ")
x = len(bank_account) 
result = ( 'X' * (len(bank_account )-4) ) + bank_account[-4:]
print(result)

