def checker(ij):
    count = 0
    for i in range(len(l)):
        if (count - l[i]) % m >= ij:
            if l[i] > count:
                count = l[i]
            else:
                return False
    return True


(n, m) = input().split()
(n, m) = [int(n), int(m)]
l = [int(i) for i in input().split()]
beg = -1
last = m
while beg < last - 1:
    mid = (beg + last) // 2
    counter = checker(mid)
    if counter:
        last = mid
    else:
        beg = mid
print(beg)
