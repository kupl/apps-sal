(n, k) = list(map(int, input().split()))
sum = 0
for i in range(n):
    if int(input()) % k == 0:
        sum += 1
print(sum)
