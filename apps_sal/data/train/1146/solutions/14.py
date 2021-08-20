def cp(l, d):
    l.sort()
    count = 0
    i = 0
    while i < len(l) - 1:
        if l[i + 1] - l[i] <= d:
            count += 1
            i += 2
        else:
            i += 1
    return count


(n, d) = map(int, input().split())
l = list((int(input()) for _ in range(n)))
print(cp(l, d))
