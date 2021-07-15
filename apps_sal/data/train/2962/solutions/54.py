def divisible_by(numbers, divisor):
    '''just use list comprehension daughter'''
    return [number  for number in numbers if number%divisor==0]
