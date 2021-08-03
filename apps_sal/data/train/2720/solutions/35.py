def solution(digits):
    n = 0
    e = len(digits) - 1
    for x in range(0, len(digits) - 1):
        if int(digits[x:x + 5]) > n:
            n = int(digits[x:x + 5])
        else:
            continue
    return n
