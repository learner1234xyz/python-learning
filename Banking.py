
BB = 0
MM = 0
inpt=0
name = input("Insert Name: ")
print("Welcome", name)
#add age verification
while True:
    # Display commands
    print("\nCommands Below:")
    print("Add")
    print("Sub")
    print("View")
    print("Logout")
    inpt = input("\nWhat Would You Like To Do: ").strip().lower()
    if inpt == "sub":
        if BB > 0:
            print("Brokeass Fuck Off")
        else:
            print("Current Balance is:", BB)
            MM = int(input("Amount: "))
            BB = BB - MM
            print("New Balance Is:", BB)
    
    elif inpt == "add":
        MM = int(input("How much money do you wish to deposit: "))
        BB = BB + MM
        print("New Balance Is:", BB)
    
    elif inpt == "view":
        print("Current Balance Is:", BB)
    
    elif inpt == "logout":
        break

    else:
        print("Invalid Command")
