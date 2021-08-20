def get_a_down_arrow_of(n):
    answer = ''
    for i in range(n, 0, -1):
        spaces = ' ' * (n - i)
        half1 = ''.join((str(x % 10) for x in range(1, i + 1)))
        half2 = half1[::-1]
        answer += spaces + half1 + half2[1:] + '\n' * (i > 1)
    return answer
