n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    if(i%2==1 and l[i]%2==0):
        print("False")
        break
else:
    print("True")