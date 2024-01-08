while True:
    print('''Enter the choice:
           1.Addition
           2.Subraction
           3.multiplication
           4.Division
           ''')
    choice=int(input("enter the choice :"))

    if choice == 1:
        n1=int(input("enter the 1st number "))
        n2=int(input("enter the 2nd number "))
        add=n1+n2
        print("the addition is " ,add)
    elif choice == 2:
        n1=int(input("enter the 1st number "))
        n2=int(input("enter the 2nd number "))
        sub=n1-n2
        print("the subtraction is " ,sub)
    elif choice == 3:
        n1=int(input("enter the 1st number "))
        n2=int(input("enter the 2nd number "))
        mul=n1*n2
        print("the multiplication is " ,mul)
    elif choice == 4:
        n1=int(input("enter the 1st number "))
        n2=int(input("enter the 2nd number "))
        div=n1/n2
        print("the division is " ,div)
    else:
        print("enter proper input")
               
