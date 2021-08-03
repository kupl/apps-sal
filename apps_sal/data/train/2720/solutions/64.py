def solution(digits):
    max = 0
    for i in range(len(str(digits)) - 4):
        tmp = int(str(digits)[i:i + 5])
        if tmp > max:
            max = tmp
    return max
