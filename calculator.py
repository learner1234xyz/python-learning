inpt = 0
num1 = 0
oper=0
num2 = 0
print ("welcome to tristans amazing calculator")
print ("Operations Below")
print (" ")
print ("a = addition")
print ("s = subtraction")
print ("m = multiplication")
print ("d = division")
inpt=input("operation  ")
num1=int(input("number1  "))
num2=int(input("number2  "))
print (type(inpt))
if inpt=="a":
    print(num1+num2)
elif inpt=="s":
    print(num1-num2)
elif inpt=="m":
    print(num1*num2)
elif inpt == "d":
    if num2 != 0:  # Check for division by zero
        print(num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operation")