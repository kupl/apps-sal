def scramble(s1, s2):
    a1 = 26 * [0]
    for c in s1:
        a1[ord(c) - 97] += 1

    for c in s2:
        a1[ord(c) - 97] -= 1
        if a1[ord(c) - 97] < 0:
            return False
    return True
