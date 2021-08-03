n, q = map(int, input().split())
l = {}
for i in range(n):
    a, b = input().split()
    l[a] = b
for i in range(q):
    s = input().strip()
    if('.' in s):
        s = s.split('.')
        x = s[-1]
        if(x in l):
            print(l[x])
        else:
            print('unknown')
    else:
        print('unknown')
