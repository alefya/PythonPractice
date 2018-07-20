import random
a=[1,2,3,4,5,10,5,5,5,5]
b=[1,3,5,7,5,5,5,5]
d=random.sample(range(1,30),7)
print (d)

c=[]
for eachItem in a:
    if eachItem in b:
        c.append(eachItem)


print (c)
        
print (set(a) & set(b))

commonList = set();
[commonList.add(x) for x in a for y in b if x == y]    
print(list(commonList))

