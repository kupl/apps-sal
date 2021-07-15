n=int(input())
s=input()
count=0
l=list(s)
for i in range(0,n-1):
    if l[i]==l[i+1]:
        count=count+1
print(count)
