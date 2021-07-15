# cook your dish here
n=int(input())
s=input()
s=list(s)
# print(s)
ans=[]
ans.append(s[0])
for i in range(1,len(s)):
    if s[i]!=ans[-1]:
        ans.append(s[i])
# print(ans)
print(len(s)-len(ans))
        

