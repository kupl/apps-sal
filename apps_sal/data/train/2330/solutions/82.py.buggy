s = input()
n = len(s)
if s[0] == "0" or s[-1] == "1":
    print((-1))
    return
for i in range(n // 2 + 1):
    if s[i] != s[-2 - i]:
        print((-1))
        return

print((1, 2))
now = 2
for i in range(1, n - 1):
    if s[i] == "0":
        print((now, i + 2))
    else:
        print((now, i + 2))
        now = i + 2
