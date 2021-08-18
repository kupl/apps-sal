import sys

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

arr = [0] * 26
pref = []

for i in range(len(s)):
    for j in range(26):
        if alph[j] == s[i]:
            arr[j] += 1
            break
    pref += [arr[:]]


q = int(sys.stdin.readline().strip())

for _ in range(q):
    r, c = sys.stdin.readline().strip().split()

    for i in range(26):
        if alph[i] == c:
            ind = i
            break

    r = int(r)

    prev = ((r - 1)**2 + r - 1) // 2

    done = prev % len(s)

    ans = 0
    rem = (len(s) - done) % len(s)

    if r <= rem:
        print(pref[done + r - 1][ind] - pref[done - 1][ind])
        continue

    if rem != 0:
        ans += pref[-1][ind] - pref[done - 1][ind]
        r -= rem

    ans += pref[-1][ind] * (r // len(s))
    r %= len(s)

    if r != 0:
        ans += pref[r - 1][ind]

    print(ans)
