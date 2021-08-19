test = int(input())
while test:
    (n, k) = map(int, input().split())
    print(2 * n - 2 * (n - 1) / k)
    test -= 1
