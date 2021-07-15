
n = int(input())
final = []
for temp in range(n):
    s = input()
    res=""
    for i in range(len(s)):
        if (s[i]>='a' and s[i]<='z') or (s[i]>='A' and s[i]<='Z') or (s[i]==' '):
            res+=s[i]
    res=res.split(" ")
    res=res[::-1]
    res=" ".join(res)
    final.append(res)
x = len(final)
while(x>0):
    x=x-1
    print(final[x])
