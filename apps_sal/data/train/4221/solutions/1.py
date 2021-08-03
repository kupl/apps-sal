def count_targets(n, s):
    return sum(s[i] == s[i - n] for i in range(n, len(s)))
