def solution(digits):
    largest = 0
    for i in range(len(digits)-4):
        a = int(digits[i:i+5])
        if (a > largest):
            largest = a
    return largest;
