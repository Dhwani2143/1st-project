while True:
    print("Calculator")
    print("1.Add")
    print("2.Substract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    choice=int(input("Enter Choice(1-5): "))
    if choice==1:
        a=int(input("Enter number1: "))
        b=int(input("Enter number2: "))
        c=a+b
        print("Sum=",c)
    elif choice==2:
        a=int(input("Enter number1: "))
        b=int(input("Enter number2: "))
        c=a-b
        print("Difference=",c)
    elif choice==3:
        a=int(input("Enter number1: "))
        b=int(input("Enter number2: "))
        c=a*b
        print("Product=",c)
    elif choice==4:
        a=int(input("Enter number1: "))
        b=int(input("Enter number2: "))
        c=a/b
        print("Quotient=",c)
    elif choice==5:
        print("Successfully exit")
        exit()
        break
    else:
        print("Invalid output")
        
else:
    print('Invalid output')
