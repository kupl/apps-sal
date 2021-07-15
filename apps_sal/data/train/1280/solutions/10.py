# cook your dish here
t=int(input())
for _ in range(t):
    str1=input().strip()
    n=len(str1)
    res=0
    for i in range(0,int(n/2)):
        #print(ord(str1[i]),ord(str1[n-i-1]))
        res += abs(ord(str1[i])-ord(str1[n-i-1]))
    print(res)

