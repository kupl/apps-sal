for _ in range(int(input())):
    n, k, x = map(int, input().split())
    if k == 1:
        for _ in range(n):
            print(x, end=" ")
        print()
        continue
    for i in range(n):
        if i % k == 0:
            print(x, end=" ")
        else:
            print(0, end=" ")
    print()
