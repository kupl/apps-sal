n = int(input())
while n > 0:
    n = n - 1
    (p, k) = list(map(int, input().split()))
    sum = 0
    i = k
    while i <= p:
        sum = sum + i % 10
        i = i + k
    print(sum)
