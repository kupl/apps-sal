def find_missing_number(s):
    if not s:
        return 0
    try:
        arr = list(map(int, s.split()))
        mi, mx = min(arr), max(arr)
        for i in range(1, mx + 1):
            if i not in arr:
                return i
        return 0
    except:
        return 1
