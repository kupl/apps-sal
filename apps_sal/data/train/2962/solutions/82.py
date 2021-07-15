def divisible_by(numbers, divisor):
    new=[]
    for item in numbers:
        if item%divisor==0:
            new.append(item)
    return new
