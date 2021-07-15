def solution(number):
    [threes, fives, fifteens] = [int((number-1)/div) for div in [3, 5, 15]]
    return [threes-fifteens, fives-fifteens, fifteens]

