# cook your dish here
n=int(input())
for _ in range(n):
    s=input()
    if s[0]=='0':
        print(0)
    else:
        c=0
        flag=0
        for i in range(1,len(s)):
            if(s[i]=='0'):
               c+=1
               flag=1
            if(s[i]=='1' and flag==1):
                break
        print(c)
