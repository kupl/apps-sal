# coding: utf-8
n, m = [int(i) for i in input().split()]
languages = []
ans = 0
for i in range(n):
    tmp = set([int(j) for j in input().split()[1:]])
    if tmp:
        languages.append(tmp)
    else:
        n -= 1
        ans += 1
i = 0
while i < n:
    j = i + 1
    while j < n:
        if languages[i] & languages[j]:
            languages[i] = languages[i] | languages[j]
            del(languages[j])
            n -= 1
        else:
            j += 1
    i += 1
i = 0
while i < n:
    j = i + 1
    while j < n:
        if languages[i] & languages[j]:
            languages[i] = languages[i] | languages[j]
            del(languages[j])
            n -= 1
        else:
            j += 1
    i += 1
if n:
    ans += n - 1
print(ans)
