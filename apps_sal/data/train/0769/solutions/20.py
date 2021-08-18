t = int(input())
while t > 0:
    t -= 1
    a, b = list(map(int, input().split()))
    ans = 1
    for i in range(2, a):
        if a % i == 0 and b % i == 0:
            ans = i
    print(ans)
