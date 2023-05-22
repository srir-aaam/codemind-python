n=int(input())
l=list(map(int,input().split()))
s=0
s1=0
for i in range(n):
    if(l[i]%2==0):
        s=s+l[i]
for j in range(n):
    if(l[j]%2==1):
        s1=s1+l[j]
print(abs(s-s1))