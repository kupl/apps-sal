a = int(input())
for i in range(0, a):
    n = int(input())
    x = list(map(int, input().split()))
    print(min(x) * (n - 1))
