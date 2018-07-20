divisor=int(input("Enter the number "))
x=range(2,divisor)
divisorList=[1,divisor]

for xItem in x:
    if divisor%xItem==0:
        divisorList.append(xItem)

print (divisorList)

