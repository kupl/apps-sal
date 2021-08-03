n, k = list(map(int, input().split()))
n -= 1
val = n // k
div = n % k
i = 2
if div == 0:
    print(val * 2)
elif div == 1:
    print(val * 2 + 1)
else:
    print((val + 1) * 2)
for a in range(k):
    print(1, i)
    for j in range(val - 1):
        print(i, i + 1)
        i += 1
    i += 1
j = i - 1
while(div):
    print(j, i)
    i += 1
    j -= val
    div -= 1
