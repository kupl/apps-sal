def pattern(n):
    mid = ''
    nums = '1234567890' * n
    for i in range(n):
        mid += nums[i]
    mid += mid[-2::-1]
    d = []
    for i in range(n - 1):
        d.append(''.join(mid.rsplit(mid[i:-i - 1], 1)).center(2 * n - 1))
    d.append(mid)
    for j in d[-2::-1]:
        d.append(j)
    return '\n'.join(d)
