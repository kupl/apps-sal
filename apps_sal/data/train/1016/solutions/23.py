for _ in range(int(input())):
    count = 0
    n = int(input())
    for i in range(n):
        x, y = list(map(int, input().split()))
        if y - x > 5:
            count = count + 1
    print(count)
