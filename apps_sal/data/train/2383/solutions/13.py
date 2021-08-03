for t in range(int(input())):
    a, b = map(int, input().split())
    l = (max(max(a, b), 2 * min(a, b)))
    print(l**2)
