def missing(nums, str):
    s = str.replace(' ', '')
    arr = sorted(nums)
    return 'No mission today' if arr[-1] >= len(s) else ''.join(s[a] for a in arr).lower()
