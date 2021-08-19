def solution(digits):
    result = -1
    for i in range(len(digits)):  # for each digit in the range of the digits (= without starting over, it will start and only go untill the last number, then no more checks)
        # new number, starting one plus up to 4 next (index and untill index+5)
        current = int(digits[i: i + 5])
        # if new number is higher than a previous check, it's a new result (check starts as -1, so every FIRST check is the new result)
        if current >= result:
            result = current  # it will loop untill the next check isn't higher; then it finishes and returns the result
    return result
