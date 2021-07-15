import itertools
import bisect

n, A, cf, cm, m = [int(x) for x in input().split()]
skills = [int(x) for x in input().split()]
sorted_skills = list(sorted((k, i) for i, k in enumerate(skills)))
bottom_lift = [0 for i in range(n)]
for i in range(1, n):
    bottom_lift[i] = bottom_lift[i-1] + i * (sorted_skills[i][0] - sorted_skills[i-1][0])
root_lift = [0 for i in range(n+1)]
for i in range(1, n+1):
    root_lift[i] = root_lift[i-1] + A - sorted_skills[n-i][0]

max_level = -1
for i in range(n+1):
    money_left = m - root_lift[i]
    if money_left < 0: break
    k = min(bisect.bisect(bottom_lift, money_left), n-i)
    money_left -= bottom_lift[k-1]
    min_level = min(A, sorted_skills[k-1][0] + money_left//k) if k > 0 else A
    level = cf*i + cm*min_level
    if max_level < level:
        max_level = level
        argmax = i
        argmax_min_level = min_level
        argmax_k = k

ans = [0 for i in range(n)]
for i, skill in enumerate(sorted_skills):
    if i < argmax_k:
        ans[skill[1]] = argmax_min_level
    elif i >= n - argmax:
        ans[skill[1]] = A
    else:
        ans[skill[1]] = skill[0]

print(max_level)
for a in ans:
    print(a, end = ' ')
    

