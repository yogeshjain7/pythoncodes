string="madd"
string_lower=string.lower()
reverse=""
for char in string_lower:
    reverse=char+reverse
if reverse==string_lower:
    print("it is palindrome")
else:
    print("not an palindrome")
