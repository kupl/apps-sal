def shuffled_array(s):
    for i in range(len(s)):
        k = s[:i] + s[i+1:]
        if sum(k) == s[i]:
            return sorted(k)
