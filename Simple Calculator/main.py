first=input("Enter first number:")
operator=input("Enter any operator(+,-,*,%,/,**):")
second=input("Enter second number")
a=int(first)
b=int(second)
if operator=='+':
    print(a+b)
elif operator=='-':
    print(a-b)
elif operator=='*':
    print(a*b)
elif operator=='/':
    print(a/b)
elif operator=='%':
    print(a%b)
elif operator=='**':
    print(a**b)
else:
    print("Invalid operation")
