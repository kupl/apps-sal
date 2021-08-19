for i in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    x = 0
    for j in range(n):
        x ^= lst[j]
    print(x)
