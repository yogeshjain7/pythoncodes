a=int(input("enter 1st no\n"))
b=int(input("enter 2nd no\n"))
op=input("enter the operator\n")
match op:
    case '+':print(a+b)
    case '-':print(a-b)
    case '*':print(a*b)
    case '/':print(a/b)
    case '%':print(a%b)
    case '**':print(a**b)


