ss = 0
for _ in range(int(input())):
    s = list(map(int, input().split()))
    ss += len(list(range(s[0], s[1] + 1)))
print(ss % (10 ** 9 + 7))
