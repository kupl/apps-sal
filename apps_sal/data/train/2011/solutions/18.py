n = int(input())


def digit_sum(x):
    if x < 0:
        return 0
    res = 0
    while x:
        res += x % 10
        x = x // 10
    return res


res = []
for i in range(200):
    m = n - i
    if digit_sum(m) == i:
        res.append(m)

print(len(res))
while res:
    print(res.pop())
