def solve(str1, str2):
    s = set(str1) - set(str2)
    return 1 if any(c for c in s if str1.count(c) > 1) else 2 
