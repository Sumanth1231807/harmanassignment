def list(a):
    return a==a[::-1]
x=input("enter word:")
str=list(x)
print(str)
if str:
    print("is palindrome")
else:
    print("it is not palindrome")


