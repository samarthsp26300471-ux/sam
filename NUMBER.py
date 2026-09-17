A=int(input("Enter the first number="))
B=int(input("Enter the secound number="))
C=int(input("Enter the third number="))
if A>B and C>B:
    print(f"{B} is the smallest number")
elif A>C and B>C:
    print(f"{C} is the smallest number")
else:
    print(f"{A} is the smallest number")        
