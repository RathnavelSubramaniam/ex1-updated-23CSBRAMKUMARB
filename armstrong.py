n=int(input())
tep=n
sum=0
while tep>0:
    d=tep%10
    sum=sum+d**3
    tep //=10
if sum==n:
    print("armstrong")
else:
    print("not armstrong")