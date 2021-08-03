def solution(digits):
    biggest = 0
    five = ""
    for loop in range(len(digits) - 4):
        five = (digits[loop] + digits[loop + 1] + digits[loop + 2] + digits[loop + 3] + digits[loop + 4])
        if biggest < int(five):
            biggest = int(five)
    return biggest
