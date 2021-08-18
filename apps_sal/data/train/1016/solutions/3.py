for _ in range(int(input())):
    n = int(input())
    c = 0
    for i in range(n):
        s, j = map(int, input().split())
        if abs(s - j) > 5:
            c = c + 1
    print(c)
