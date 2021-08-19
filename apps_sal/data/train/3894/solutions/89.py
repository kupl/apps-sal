def solve(s):
    s_upper = s.upper()
    s_lower = s.lower()
    if s == s_upper:
        return s
    elif s == s_lower:
        return s
    lower_change = 0
    upper_change = 0
    for i in range(0, len(s)):
        if s_upper[i] != s[i]:
            upper_change += 1
        if s_lower[i] != s[i]:
            lower_change += 1
    if upper_change < lower_change:
        return s_upper
    return s_lower
