BB = 0
MM = 0
name = input("Insert Name: ")
print("Welcome", name)

# Add age verification logic here

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
            print("Insufficient funds. Please add money.")
        else:
            print("Current Balance is:", BB)
            MM = int(input("Amount: "))
            BB -= MM
            print("New Balance Is:", BB)
    
    elif inpt == "add":
        MM = int(input("How much money do you wish to deposit: "))
        BB += MM
        print("New Balance Is:", BB)
    
    elif inpt == "view":
        print("Current Balance Is:", BB)
    
    elif inpt == "logout":
        break

    else:
        print("Invalid Command")
