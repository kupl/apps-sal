# cook your dish here
x=input()
lst=x.split()
n=int(lst[0])
m=int(lst[1])
l=list()
for i in range(n):
    l.append(int(input()))
l.sort()
k=0
mn=100000000000000
while m+k<=n:
        s=l[m+k-1]-l[k]
        if mn>s:
            mn=s
        k+=1
print(mn)
