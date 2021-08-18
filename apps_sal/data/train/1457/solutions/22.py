
n, k = list(map(int, input().split()))
i = 1
sum = 0
while i <= n:

    z = int(input())
    if z % k == 0:
        sum = sum + 1
        i = i + 1
    else:
        i = i + 1

print(sum)
