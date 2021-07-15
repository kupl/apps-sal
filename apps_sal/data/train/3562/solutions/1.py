def count_inversion(s):
    return sum(s[i] > s[j]
               for i in range(len(s) - 1)
               for j in range(i + 1, len(s)))
