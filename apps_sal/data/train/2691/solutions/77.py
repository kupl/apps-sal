def solve(s):
    digits = '0123456789'
    res = []
    temp_nums = ''
    for i in s:
        if i in digits:
            temp_nums += i
        if i not in digits:
            if len(temp_nums) > 0:
                res += [int(temp_nums)]
            temp_nums = ''
    if len(temp_nums) > 0:
        res += [int(temp_nums)]
    return max(res)
