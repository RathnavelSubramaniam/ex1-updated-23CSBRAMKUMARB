#wiht ifelse
a=int(input())
if a%4==0:
    print("year is leap ")
else:
    print("year is not leap")
#with function
def leap():
    if(a%4==0):
        print("leap year")
    else:
        print("not leap year")
print(leap())