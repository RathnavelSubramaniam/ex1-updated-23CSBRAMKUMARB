#wihtout Function
h=int(input())
b=int(input())
area=0.5*h*b
print(area)
#with Function
def area():
    h=int(input())
    b=int(input())
    areaa=b*h*0.5
    return areaa
print(area())