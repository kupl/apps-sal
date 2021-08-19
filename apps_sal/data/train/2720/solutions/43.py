def solution(digits):
    sl = 0
    res_list = []
    for count in range(len(digits) - 1):
        res_list.append(int(digits[sl:sl + 5]))
        sl += 1
    return max(res_list)
