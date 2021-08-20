def isSubSetSum(a, n, w):
    subset = [[0 for x in range(n + 1)] for y in range(w + 1)]
    for i in range(n + 1):
        subset[0][i] = 1
    for i in range(1, w + 1):
        subset[i][0] = 0
    for i in range(1, w + 1):
        for j in range(1, n + 1):
            subset[i][j] = subset[i][j - 1]
            if i >= a[j - 1]:
                if subset[i][j] == 1 or subset[i - a[j - 1]][j - 1] == 1:
                    subset[i][j] = 1
    return subset[w][n]


(n, q) = input().split()
(n, q) = (int(n), int(q))
a = input().split()
a = [int(x) for x in a]
while q > 0:
    s = input().split()
    s = [int(x) for x in s]
    l = s[1]
    r = s[2]
    if s[0] == 1:
        a[l - 1] = r
    elif s[0] == 2:
        i = l - 1
        j = r - 1
        while i <= j:
            swap = a[i]
            a[i] = a[j]
            a[j] = swap
            i += 1
            j -= 1
    else:
        w = s[3]
        b = a[l - 1:r]
        if isSubSetSum(b, len(b), w) == 1:
            print('Yes')
        else:
            print('No')
    q = q - 1
