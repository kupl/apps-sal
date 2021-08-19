def mystery_range(s, n):
    ones = int((3 * n - 90 - len(s)) / 2)
    if '100' in s and ones > 0:
        hundreds = int((len(s) - 180 - ones) / 3)
        return [10 - ones, 99 + hundreds]
    elif '100' in s:
        hundreds = len(s) - 2 * n
        tens = n - hundreds
        return [100 - tens, 99 + hundreds]
    elif '10' in s:
        tens = len(s) - n
        ones = n - tens
        return [10 - ones, 9 + tens]
    elif len(s) == n:
        nums = list(map(int, s))
        return [min(nums), max(nums)]
    elif len(s) == 2 * n:
        nums = [int(s[i:i + 2]) for i in range(0, len(s), 2)]
        return [min(nums), max(nums)]
