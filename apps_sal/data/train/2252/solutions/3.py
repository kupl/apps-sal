from collections import Counter

n = int(input())

mp = Counter({'': 0})

for i in range(n):
    string = input()
    occ = [0] * 26
    for c in string:
        occ[ord(c) - ord('a')] += 1
        if occ[ord(c) - ord('a')] == 2:
            occ[ord(c) - ord('a')] = 0
    clean = []
    for idx in range(26):
        while occ[idx] > 0:
            clean.append(chr(idx + ord('a')))
            occ[idx] -= 1

    mp[''.join(clean)] += 1

ans = 0


def combs(n):
    return n * (n - 1) // 2


for key in mp:
    if len(key) == 1:
        ans += combs(mp[key]) + mp[key] * mp['']
    elif len(key) == 0:
        ans += combs(mp[key])
    else:
        ans += combs(mp[key])
        for idx in range(len(key)):
            ans += mp[key] * mp[key[0:idx] + key[idx + 1:]]

print(ans)

