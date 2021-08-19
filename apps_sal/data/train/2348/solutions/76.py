N = int(input())
xs = list(map(int, input().split()))
L = int(input())
parent = [-1] * N
right = 0
for left in range(N):
    while right < N and xs[right] - xs[left] <= L:
        right += 1
    parent[left] = right - 1
ancestor = [parent]
for _ in range(N.bit_length() + 2):
    tmp = [ancestor[-1][anc] for anc in ancestor[-1]]
    ancestor.append(tmp)
Q = int(input())
answers = []
for _ in range(Q):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    if a == b:
        answers.append(0)
        continue
    if a > b:
        (a, b) = (b, a)
    ans = 0
    for k in range(len(ancestor) - 1, -1, -1):
        if ancestor[k][a] < b:
            ans += 1 << k
            a = ancestor[k][a]
    ans += 1
    answers.append(ans)
print(*answers, sep='\n')
