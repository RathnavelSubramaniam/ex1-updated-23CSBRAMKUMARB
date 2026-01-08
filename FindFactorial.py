#with loop
f=1
n=int(input())
for i in range(1,n+1):
    f=f*i
print(f)
#recursion
f=1
n=int(input("input:"))
if(n==0 or n==1):
    return 1
else:
    return f