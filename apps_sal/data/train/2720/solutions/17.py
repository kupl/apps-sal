def solution(digits):
    max = 99999
    while True:
        if str(max) in digits:
            return max
        else:
            max -= 1

    return 0
