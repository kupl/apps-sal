N = int(input())
num = 0
result = 0
min = 10000000000
for i in range(N):
    (a, b) = list(map(int, input().split()))
    if a > b:
        if b < min:
            min = b
            num = 1
    result += a
if num == 0:
    print(0)
else:
    result -= min
    print(result)
