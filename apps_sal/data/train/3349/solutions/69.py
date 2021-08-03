def find_missing_number(s):
    try:
        s = sorted(map(int, s.split()))
    except:
        return 1
    for i, j in enumerate(s[:-1]):
        if j + 1 != s[i + 1]:
            return j + 1
    return 0 if not s or s[0] == 1 else 1
