t = int(input())
for i in range(t):
    n = int(input())
    hello = list(map(int, input().strip().split()))
    count = 0
    for i in range(len(hello) - 1):
        if hello[i + 1] > hello[i]:
            hello[i + 1] = hello[i]
            count = count + 1
    print(n - count)
