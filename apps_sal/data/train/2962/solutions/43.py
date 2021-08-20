def divisible_by(numbers, divisor):
    arr1 = []
    for num in numbers:
        if num % divisor == 0:
            arr1.append(num)
    return arr1
