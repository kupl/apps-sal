t = int(input())
for _ in range(t):
    (n, k, v) = list(map(int, input().split()))
    l = list(map(int, input().split()))
    count = sum(l)
    total = v * (n + k)
    num = total - count
    if total <= count:
        print('-1')
    elif num % k != 0:
        print('-1')
    else:
        print(int(num / k))
