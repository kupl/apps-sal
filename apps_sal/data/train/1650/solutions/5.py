def find_all(sum_dig, digits):
    if sum_dig > digits * 9:
        return []
    num = [1] * digits
    res = []
    while num[0] != 10:
        if sum(num) == sum_dig:
            res.append(int(''.join(map(str, num))))
        for i in range(digits - 1, -1, -1):
            num[i] += 1
            if num[i] != 10:
                break
        for i in range(1, digits):
            if num[i] == 10:
                num = num[:i] + [num[i - 1]] * (digits - i)
                break
    return [len(res), res[0], res[-1]]
