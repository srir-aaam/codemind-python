n=int(input())
s=0
a=abs(n)
while a>0:
    s=s*10+(a%10)
    a=a//10
if(n<0):
    print(-1*s)
else:
    print(s)