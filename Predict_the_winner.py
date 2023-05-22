n=int(input())
lst=list(map(int,input().split()))
s=0
s1=0
for i in lst:
    if(i%2==0):
        s=s+i
for j in lst:
    if(j%2!=0):
        s1=s1+j
if((abs(s-s1))%4==0):
    print("X")
else:
    print("Y")