for i in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    z = max(a) + k
    m = min(a) - k
    sum = abs(z) + abs(m)
    print(sum)
