for i in range(int(input())):
    n = int(input())
    s = input()
    a = set()
    for j in s:
        a.add(j)
    a = list(a)
    a.sort()
    print(a[0])
