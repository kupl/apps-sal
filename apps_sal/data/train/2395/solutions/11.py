def go():
    # n,k = map(int,input().split())

    n = int(input())
    x= input()
    a=[]
    b=[]
    i=0
    while i<n and x[i]!='1':
        if x[i]=='2':
            a.append('1')
            b.append('1')
        else:
            a.append('0')
            b.append('0')
        i+=1

    if i<n:
        a.append('1')
        b.append('0')
        i+=1

    while i<n:
        a.append('0')
        b.append(x[i])
        i+=1

    return ''.join(a) + '\n' + ''.join(b)





# x,s = map(int,input().split())
t = int(input())
# t=1
ans=[]
for _ in range(t):
    # go()
    ans.append(str(go()))

print('\n'.join(ans))
