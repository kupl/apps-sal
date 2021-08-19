def find_missing_number(s):
    if any((x.isalpha() or x == '_' for x in s)):
        return 1
    s = sorted(map(int, s.split()))
    return 0 if not s or all((x in s for x in range(1, s[-1] + 1))) else min(set(range(1, s[-1] + 1)) - set(s))
