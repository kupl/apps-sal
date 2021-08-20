def series_sum(n):
    answer = 0
    for number in range(n):
        answer += 1 / (1 + number * 3)
    return str(format(answer, '.2f'))
