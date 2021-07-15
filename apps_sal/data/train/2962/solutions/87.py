def divisible_by(numbers, divisor):
    mt = []        
    [mt.append(x) for x in numbers if x % divisor == 0]
    return mt
