def divisible_by(numbers, divisor):
    return [x for x in numbers if x % divisor == 0]
    #return list(filter(lambda x: x % divisor == 0, numbers))

