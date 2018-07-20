inputString=input("Enter the string to be tested \n")

stringLength=len(inputString)

flag=True
i=0
while i < (stringLength/2):
    if inputString[i]!=inputString[stringLength-i-1]:
        flag=False
    i=i+1   

print ("Palindrome status "+str(flag))


rev=str(inputString[::-1])
if rev==inputString:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
