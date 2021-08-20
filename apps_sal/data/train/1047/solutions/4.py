T = int(input())
for i in range(T):
    N = int(input())
    l1 = []
    l2 = []
    for j in range(N):
        (a, b) = map(int, input().split())
        l1.append(a - b)
        l2.append(a + b)
    l1.sort()
    l2.sort()
    m1 = 100000000000000000000000
    for j in range(1, len(l1)):
        if l1[j] - l1[j - 1] < m1:
            m1 = l1[j] - l1[j - 1]
    m2 = 1000000000000000000000
    for j in range(1, len(l2)):
        if l2[j] - l2[j - 1] < m2:
            m2 = l2[j] - l2[j - 1]
    if min(m1, m2) % 2 == 0:
        print(min(m1, m2) // 2)
    else:
        print(min(m1, m2) / 2)
