print("\n OPTIONS")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice=int(input("Enter the operation number to be performed: "))

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

if choice==1:
    add=a+b
    print("Addition = ",add)
elif choice==2:
    sub=a-b
    print("Subtraction = ",sub)
elif choice==3:
    mul=a*b
    print("Multiplication = ",mul)
elif choice==4:
    div=a/b
    print("division = ",div)
else:
    print("Invalid choice!!!")
