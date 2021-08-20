n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort()
mini = abs(-n // 2)
(f_l, s_l) = (lst[:mini], lst[mini:])
ans = 0
j = 0
i = 0
extra = 0
while i < len(f_l) and j < len(s_l):
    if f_l[i] * 2 <= s_l[j]:
        ans += 1
        i += 1
        j += 1
    else:
        extra += 1
        j += 1
ans += len(s_l) - j + len(f_l) - i + extra
print(ans)
