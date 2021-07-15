def shuffled_array(s):
    s.sort()
    for i in range(len(s)):
        if s[i] == sum(s[:i]+s[i+1:]):
            return s[:i]+s[i+1:]
