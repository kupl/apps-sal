# cook your dish here
t = int(input())
for z in range(t):
    a, b = [int(x) for x in input().split()]
    s = input().split()
    x = []
    for i in range(b):
        y = input().split()
        x = x + y
    l = set(x)
    for i in s:
        if i in l:
            print("YES", end=' ')
        else:
            print("NO", end=' ')
    print()
