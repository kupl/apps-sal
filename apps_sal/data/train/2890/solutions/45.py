def multiples(m, n):
    answer = []
    i = 1
    while i <= m:
        x = n * i
        answer.append(x)
        i += 1
    return answer
