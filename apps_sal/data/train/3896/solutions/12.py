def solution(number):
    return sum(set(range(0, number, 3)) | set(range(0, number, 5)))
