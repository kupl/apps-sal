for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in range(n):
        a, b = list(map(int, input().split()))
        if abs(a - b) > 5:
            count += 1
    print(count)
