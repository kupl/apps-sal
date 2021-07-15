# cook your dish here
for i in range(int(input())):
    n, d = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = []
    for t in reversed(range(n)):
        x = d//a[t]
        b.append(x*a[t])
        d = x*a[t]
        
    print(min(b))
