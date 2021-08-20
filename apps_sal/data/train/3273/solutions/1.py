def solve(str1, str2):
    return 2 - any((str1.count(c) > 1 and c not in str2 for c in str1))
