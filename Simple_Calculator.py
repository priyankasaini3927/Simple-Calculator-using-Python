print("Welcome to Simple Calculator\n")

while True:
    print("Choose the one of the following operation\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Modulus\n6.Power\n7.Exit\n")
    choice=input("Choose the opretion: ")

    if choice=='7':
      print("Exiting...!")
      break 

    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))


    if choice=='1':
     print(f"{num1+num2}")
    elif choice=='2':
     print(f"{num1-num2}")       
    elif choice=='3':
     print(f"{num1*num2}")
    elif choice=='4':
     if num2 == 0:
        print("Error! Cannot perform divide by zero.")
     else:
        print(f"{num1/num2}")
    elif choice=='5':
      if num2 == 0:
        print("Error! Cannot perform modulus by zero.")
      else:
        print(f"{num1%num2}")
    elif choice=='6':
        print(f"{num1**num2}")        
    else:
     print("Invalid Input")