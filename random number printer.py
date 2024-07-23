import random

c=random.randint(1,100)
b = 0
while True:
    a=random.randint(1,100)
    print (a)
    b = b+1
    if a==c:
        print("found", c)
        print ("Tries Below")
        print (" ")
        print (b)
        break

