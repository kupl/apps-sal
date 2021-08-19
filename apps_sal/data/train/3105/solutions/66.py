def count_sheep(n):
    answer = ''
    for i in range(n):
        answer += '{} sheep...'.format(i + 1)
    return answer
