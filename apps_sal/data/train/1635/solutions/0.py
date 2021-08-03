def middle_permutation(string):
    s = sorted(string)
    if len(s) % 2 == 0:
        return s.pop(len(s) // 2 - 1) + ''.join(s[::-1])
    else:
        return s.pop(len(s) // 2) + middle_permutation(s)
