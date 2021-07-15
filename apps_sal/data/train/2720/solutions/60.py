def solution(digits):
    solution = int(digits[0:5])
    for index in range(1, len(digits)):
        current = int(digits[index:index+5])
        solution = current if current > solution else solution

    return solution
