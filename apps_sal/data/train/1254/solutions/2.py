# cook your dish here
t = int(input())
for z in range(t):
    n, p = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    c = [x for x in a if x >= p // 2]
    h = [x for x in a if x <= p // 10]
    if len(c) == 1 and len(h) == 2:
        print("yes")
    else:
        print("no")
