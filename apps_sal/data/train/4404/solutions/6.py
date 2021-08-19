def compare(s1, s2):
    (n1, n2) = ([int(i) for i in s1.split('.')], [int(i) for i in s2.split('.')])
    l = min(len(n1), len(n2))
    for i in range(l):
        if n1[i] == n2[i]:
            continue
        return 1 if n1[i] > n2[i] else -1
    if any(n1[l:] + n2[l:]):
        return 1 if len(n1) > len(n2) else -1
    return 0
