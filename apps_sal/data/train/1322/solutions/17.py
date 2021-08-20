t = int(input())
for i in range(t):
    (n, k) = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    a = l[k - 1]
    j = 0
    count = 0
    while j < len(l):
        if l[j] >= a:
            count += 1
        else:
            break
        j += 1
    print(count)
