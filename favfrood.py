fav="pizza"
tries=0
hint=False
inpt=input("guess my favorite food ")
if inpt!=fav:
    print("wrong")
    inpt=input("Hint (y/n) ")
    if inpt=="y":
        print("its a junk food")
    elif inpt=="n":
        print ("ok")
    else:
        print("ok? you just lost a hint")
else:
    print("you win")
    print("tries =" ,tries)
    while True:
        tries=0
tries=tries+1
inpt=input("guess my favorite food ")
if inpt!=fav:
    print("wrong")
    inpt=input("Hint (y/n)")
    if inpt=="y":
        print("it has crust and tomato")
    elif inpt=="n":
        print ("ok")
    else:
        print("ok? you just lost a hint")
else:
    print("you win")
    print("tries =" ,tries)
    while True:
        tries=0
tries=tries+1
inpt=input("guess my favorite food ")
if inpt!=fav:
    print("wrong")
    inpt=input("Hint (y/n) ")
    if inpt=="y":
        print("it starts with a P and ends with an A ")
    elif inpt=="n":
        print ("ok")
    else:
        print("ok? you just lost a hint")
else:
    print("you win")
    print("tries =" ,tries)
    while True:
        tries=0
tries=tries+1
while True:
    inpt=input("guess my favorite food")
    if inpt!=fav:
        print("wrong try again")
        tries=tries+1
    elif inpt==fav:
        print("you win!")
        print("tries is:",tries)
        while True:
            tries=tries