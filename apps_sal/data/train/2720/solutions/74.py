def solution(digits):
    k = 5
    ret = int(digits[0:k])
    index = 5
    while index + k < len(digits):
        temp = digits[index: index + k]
        ret = max(ret, int(temp))
        index += 1
    ret = max(ret, int(digits[index:]))
    return ret
