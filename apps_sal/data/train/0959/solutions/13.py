for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sum_ = 0
    for i in range(n // 2):
        sum_ += abs(a[i] - a[n - i - 1])
    print(sum_)
