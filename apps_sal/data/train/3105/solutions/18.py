def count_sheep(n):
    answer = []
    for x in range(1, n + 1):
        answer.append(str(x))
        answer.append(" sheep...")
    return ''.join(answer)
