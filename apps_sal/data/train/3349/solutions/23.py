def find_missing_number(s):
    if not s:
        return 0
    try:
        s = sorted((int(i) for i in s.split()))
    except:
        return 1
    return next((i + 1 for i in range(s[-1]) if i + 1 not in s), 0)
