import random
a=random.randint(1,9)
flag=False
guessedNum=input("Enter a number ")
tries=0
while flag==False:
    if int(guessedNum)==a:
        print("You guessed correctly in "+str(tries)+" tries")
        flag=True
    elif int(guessedNum)>a:
        print("Enter smaller number ")
        guessedNum=input("Enter a number ")
        tries=tries+1
    else:
        print("Enter bigger number ")
        guessedNum=input("Enter a number ")
        tries=tries+1
