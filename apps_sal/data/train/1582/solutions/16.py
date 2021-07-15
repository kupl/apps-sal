# cook your dish here
n=int(input())
s=input()
l=[]
for i in s:
    l.append(i)
ans=0
for i in range(1,len(s)):
    if l[i-1]==l[i]:
        ans+=1
print(ans)
