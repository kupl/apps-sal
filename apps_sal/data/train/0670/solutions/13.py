t = eval(input())
for _ in range(t):
    n = eval(input())
    num = [int(i) for i in input().split()]
    num.sort()
    ans = num[0]
    for i in range(1, n):
        if(num[i] != num[i - 1]):
            ans = min(ans, num[i] - num[i - 1])
    print(ans * n)
