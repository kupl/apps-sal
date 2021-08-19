t = int(input())
for i in range(t):
    (n, k) = list(map(int, input().split()))
    if n == 0:
        teacher = 0
        candies = 0
    elif k == 0:
        candies = 0
        teacher = n
    else:
        teacher = n % k
        candies = n // k
    print(candies, teacher)
