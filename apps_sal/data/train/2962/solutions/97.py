def divisible_by(numbers, divisor):
    v = 0
    answer = []
    while len(numbers) != v:
        if numbers[v] % divisor == 0:
            answer.append(numbers[v])
            v = v + 1
        else:
            v = v + 1
    return answer
