def product(numbers):
    if numbers == [] or numbers == None:
        return None
    res = 1
    for i in numbers:
        res *= i
    return res
