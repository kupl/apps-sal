def divisible_by(numbers, divisor):
    div = []
    for i in numbers:
        if i % divisor == 0:
            h = i / divisor
            div.append(i)
    return div
