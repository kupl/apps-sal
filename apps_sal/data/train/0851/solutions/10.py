# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(2 * (n - 1) * (k - 1) / k + 2)
