s = input()
n = len(s)


def check():
    if s[0] == "0" or s[-1] == "1":
        return False
    for i in range(n):
        if s[i] != s[n - i - 2]:
            return False
    return True


if not check():
    print(-1)
    return

now = 1
for i in range(n - 1):
    print(now, i + 2)
    if s[i] == "1":
        now = i + 2
