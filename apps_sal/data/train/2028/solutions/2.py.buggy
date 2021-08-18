def isPal(x):
    for i in range(len(x) // 2):
        if x[i] != x[len(x) - 1 - i]:
            return False
    return True


s = list(input())
f = {}
for c in s:
    if c in f:
        f[c] += 1
    else:
        f[c] = 1
if len(f) == 1:
    print("Impossible")
    return
elif len(f) == 2:
    if 1 in f.values():
        print("Impossible")
        return
if len(s) % 2 == 0:
    for i in range(1, len(s)):
        new = s[i:] + s[:i]
        if s != new:
            if isPal(new):
                print(1)
                return
print(2)
