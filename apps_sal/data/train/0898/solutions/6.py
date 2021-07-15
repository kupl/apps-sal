# Why do we fall ? So we can learn to pick ourselves up.

t = int(input())
for _ in range(0,t):
    m,n = map(int,input().split())
    if n < 9:
        print(0,0)
    else:
        s = '9'
        while int(s+'9') < n:
            s += '9'
        print(m*len(s),m)


"""
1
1 9


"""
