from collections import defaultdict, Counter
N = int(input())
A = [0] + list(map(int, input().split()))
C = Counter(A)
value = sorted(set(A), reverse=True)
a_to_i = defaultdict(int)
for (i, a) in enumerate(A):
    if not a_to_i[a]:
        a_to_i[a] = i
ans = [0] * (N + 1)
cnt = 0
i = N
for (x, y) in zip(value[:-1], value[1:]):
    i = min(i, a_to_i[x])
    cnt += C[x]
    ans[i] += (x - y) * cnt
print(*ans[1:], sep='\n')
