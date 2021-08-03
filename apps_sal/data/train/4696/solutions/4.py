def same_encryption(s1, s2):
    l1, l2 = str(len(s1) - 2), str(len(s2) - 2)
    while int(l1) // 10 or int(l2) // 10:
        l1, l2 = str(sum(map(int, l1))), str(sum(map(int, l2)))
    return l1 == l2 and s1[0] == s2[0] and s1[-1] == s2[-1]
