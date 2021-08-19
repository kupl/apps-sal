def mp():
    return list(map(int, input().split()))


def lt():
    return list(map(int, input().split()))


def pt(x):
    print(x)


n = int(input())
L = lt()
count = 0
i = 0
c = [None for i in range(n)]
while i < n - 1:
    j = i
    while j < n - 1 and L[j] != L[j + 1]:
        j += 1
    span = j - i + 1
    for k in range(i, i + span // 2):
        c[k] = L[i]
    for k in range(i + span // 2, j + 1):
        c[k] = L[j]
    count = max(count, (span - 1) // 2)
    i = j + 1
    if i == n - 1:
        c[i] = L[i]
print(count)
print(' '.join([str(r) for r in c]))
