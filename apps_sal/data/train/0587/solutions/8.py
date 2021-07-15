# cook your dish here
n=int(input())
a=[int(i) for i in input().split()]
for i in a:
    if i==1:
        print("2",'',end='')
    elif i==2:
        print("1",'',end='')
    else:
        b=str(bin(i)).replace('0b','')
        p=''
        l=len(b)
        if b[l-1]=='0':
            p='0'
        else:
            p='1'
        if b[l-2]=='0':
            p='1'+p
        else:
            p='0'+p
        for j in range(l-3,-1,-1):
            p=b[j]+p
        print(int(p,2),'',end='')
print()
