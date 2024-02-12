#Part 2: Create a program and print only the last four digits, replacing the first 6 by X

#Part 2: Create a program and print only the last four digits, replacing the first 6 by X + bank_account[-4:]


bank_account = input("Input your bank account ")
x = len(bank_account) 
result = ( 'X' * (len(bank_account )-4) ) + bank_account[-4:]
print(result)



elif len(bank_account) < 10:
    print("ERROR")
    bank_account = input("Please enter 10 digits")
else:
    print("Perfect, the bank account is: ","XXXXXX"+bank_account[:4])