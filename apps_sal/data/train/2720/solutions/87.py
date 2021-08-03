def solution(digits):
    largest = 0
    for i in range(len(digits) - 4):
        sliced = int(digits[i:i + 5])
        if sliced > largest:
            largest = sliced
    return largest
