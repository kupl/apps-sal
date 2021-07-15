T=int(input())
for _ in range(T):
    s=input()
    if s[0]=='0':
        print('0')
        continue
    c=0
    z=0
    for i in range(len(s)):
        if s[i]=='1' :
            if z==0:
                continue
            else:
                break
        c+=1
        z=1
    print(c)
