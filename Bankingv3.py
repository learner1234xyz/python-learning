import os

BB = 0
MM = 0
# Get the path to the user's Documents folder
documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
file_name = 'consider.txt'
file_path = os.path.join(documents_folder, file_name)

def feedback(fdback):
    try:
        print(f"Opening file {file_path} for appending...")
        with open(file_path, 'a') as file:  # Open in append mode
            print("Appending feedback to file...")
            file.write(fdback + "\n\n")  # Add two newlines for spacing
            print("Feedback appended to file.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

inpt = 0
noerror = True
name = input("Insert Name: ")
print("Welcome", name)

# Print the current working directory
print("Current working directory:", os.getcwd())
print("Feedback file will be saved to:", file_path)

while True:
    noerror = True
    print("\nCommands Below:")
    print("Add")
    print("Sub")
    print("View")
    print("Feedback")
    print("Logout")
    inpt = input("\nWhat Would You Like To Do: ").strip().lower()

    if inpt == "sub":
        if BB < 0:
            print("Brokeass Fuck Off")
        else:
            print("Current Balance is:", BB)
            while noerror:
                try:
                    MM = int(input("Amount To Remove: "))
                    BB = BB - MM
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            print("New Balance Is:", BB)

    elif inpt == "add":
        while noerror:
            try:
                MM = int(input("Amount To Deposit: "))
                BB = BB + MM
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif inpt == "view":
        print("Current Balance Is:", BB)
    
    elif inpt == "logout":
        print("We Are So Sad To See You Go", name)
        break
    
    elif inpt == "feedback":
        fdback = input("What was wrong with our services: ")
        print("Thanks!", name, "we will take this into consideration")
        feedback(fdback)  # Ensure function is called correctly

    else:
        print("Invalid Command")
