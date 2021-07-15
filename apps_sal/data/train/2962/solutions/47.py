def divisible_by(numbers, divisor):
    arr = []
    for el in numbers:
        if el % divisor==0:
            arr.append(el)
    return arr

