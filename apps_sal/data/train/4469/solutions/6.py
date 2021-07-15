def is_narcissistic(i):
    n = len(str(i))
    lst = list(str(i))
    answer = 0
    for value in lst:
        answer += int(value)**n
    return answer == i
