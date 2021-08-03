aw = [2**i for i in range(26)]
n = int(input())
d = dict()
ans = 0
for ir in range(n):
    st = input()
    es = 0
    for j in st:
        es = es ^ aw[ord(j) - 97]
    if es in d:
        ans += d[es]
    for j in range(26):
        es = es ^ aw[j]
        if es in d:
            ans += d[es]
        es = es ^ aw[j]
    if es in d:
        d[es] += 1
    else:
        d.update({es: 1})
print(ans)
