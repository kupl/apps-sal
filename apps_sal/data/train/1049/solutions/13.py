x = int(input())
for i in range(x):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    j = 0
    m = 0
    while j + k <= n:
        # print(set(l[j:j+k]),set(l))
        if m < sum(l[j:j + k]) and set(l[j:j + k]) == set(l):
            m = sum(l[j:j + k])
        j += 1
    print(m)
