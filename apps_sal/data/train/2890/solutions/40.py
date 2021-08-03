def multiples(m, n):
    result = 0
    text = []
    for i in range(1, m + 1):
        result += 1
        text.append(result * n)
    return text
