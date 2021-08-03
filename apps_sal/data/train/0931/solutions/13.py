for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    s = 0
    for item in li:
        if item % 2 == 0:
            s += item
    print(s)
