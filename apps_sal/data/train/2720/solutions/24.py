def solution(digits):
    n = len(digits)
    max = 0
    for i in range(n - 4):
        if(max < int(str(digits[i:i+5:]))):
            max = int(str(digits[i:i+5:]))
    return max
