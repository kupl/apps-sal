def same_encryption(s1, s2):
    return (s1[0], s1[-1], len(s1) % 9) == (s2[0], s2[-1], len(s2) % 9)
