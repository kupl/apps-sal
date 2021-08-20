for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    total = 0
    for i in range(0, n):
        if s[i] == 0:
            total += 1100
        elif total >= 1100:
            total -= 1000
            total += 1100
    print(total)
