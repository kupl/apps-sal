n = int(input())
cur = 2
for i in range(1, n + 1):
    tmp = ((i * (i + 1)) ** 2 - cur) / i
    tmp = int(tmp)
    print(tmp)
    cur = i * (i + 1)
