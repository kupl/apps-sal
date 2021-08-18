a = list(input())
b = list(input())
a.sort()
b.sort(reverse=True)
ans = list()
for i in a:
    ans.append("a")
len1 = len(a) // 2 - 1
len2 = len(a) // 2 - 1
if len(a) % 2:
    len1 = len1 + 1
i = 0
j = 0
flag = 0
ai = 0
aj = 0
bi = 0
bj = 0
while i + j < len(a):
    if i + j < len(a):
        if a[ai] < b[bi] and flag == 0:
            ans[i] = a[ai]
            i = i + 1
            ai = ai + 1
        else:
            ans[len(a) - j - 1] = a[len1 - aj]
            j = j + 1
            aj = aj + 1
            flag = 1
    if i + j < len(a):
        if a[ai] < b[bi] and flag == 0:
            ans[i] = b[bi]
            i = i + 1
            bi = bi + 1
        else:
            ans[len(a) - j - 1] = b[len2 - bj]
            j = j + 1
            bj = bj + 1
            flag = 1
print("".join(ans))
