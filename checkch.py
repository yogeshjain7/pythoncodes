ch=input("enter character\n")
if ch.islower():
    print("lower case")
elif ch.isupper():
    print("upper case")
elif ch.isnumeric():
    print("it is a numeric value")
else:
    print("special charcter")


