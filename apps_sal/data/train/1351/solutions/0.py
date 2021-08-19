for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    d = set()
    for i in arr:
        d.add(i)
    for i in range(n):
        if i in d:
            print(i, end=' ')
        else:
            print(0, end=' ')
    print()
