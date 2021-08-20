def bubble(l):
    (n, permutations) = (len(l), [])
    while n:
        m = 0
        for i in range(1, n):
            if l[i - 1] > l[i]:
                (l[i - 1], l[i]) = (l[i], l[i - 1])
                permutations.append(l[:])
                m = i
        n = m
    return permutations
