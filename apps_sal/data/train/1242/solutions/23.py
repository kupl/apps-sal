t = int(input())
for m in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    print(min(lst) * (n - 1))
