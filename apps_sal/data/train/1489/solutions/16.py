def findMaximumNum(st, k):
    for i in range(len(st)):
        if k < 1:
            break
        if st[i] != '9':
            st = st[0:i] + '9' + st[i + 1:]
            k -= 1
    return st


(st, m) = input().split()
k = int(m)
print(findMaximumNum(st, k))
