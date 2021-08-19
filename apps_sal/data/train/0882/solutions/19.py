a = int(input())
# list(map(int,input().split()))
for _ in range(a):
    b = input()
    b1 = set(b)
    c = input()
    s = 0
    for i in b1:
        if i in c:
            s += min(b.count(i), c.count(i))
    print(s)
