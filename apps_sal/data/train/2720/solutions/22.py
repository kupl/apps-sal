def solution(digits):
    maxi = 0
    for i in range(len(digits) - 4):
        if int(digits[i:i + 5]) > maxi:
            maxi = int(digits[i:i + 5])
    return maxi
