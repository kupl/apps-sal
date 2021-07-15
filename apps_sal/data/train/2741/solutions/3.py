def russian_peasant_multiplication(x, y):
    answer = 0
    while y:
        if y % 2:
            answer += x
        x += x
        y //= 2
    return answer
