def string_suffix(s): return sum(s[:j - i] == s[i:j] for j in range(1, len(s) + 1) for i in range(j))
