t = eval(input())
for q in range(t):
    l = eval(input())
    a = input().split()
    a = [int(x) for x in a]
    a = sorted(a)
    for i in range(l - 1):
        a[i] = a[i + 1] - a[i]
    print(min(a[0:l - 1]))
