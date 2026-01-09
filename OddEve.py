#with ifelse
print("Finding that given number is ODD or EVEN")
print()
a=int(input())
if(a%2==0):
    print("The given NUmber is even")
else:
    print("The given NUmber is Odd")
#with function
def oddeve():
    if(a%2==0):
        print("given number is even")
    else:
        print("given number is odd")
print(oddeve())