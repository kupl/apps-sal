for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in range(1, n + 1, 2):
        k = n - i + 1
        count += (k * k)
    print(count)
