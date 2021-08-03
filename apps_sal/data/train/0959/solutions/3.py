for _ in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))
    b.sort()
    c = 0
    k = a // 2
    for i in range(k):
        c += abs(b[i] - b[a - i - 1])
    print(c)
