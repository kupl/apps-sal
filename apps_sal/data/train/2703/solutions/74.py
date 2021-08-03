def square_sum(numbers):
    sum = 0

    def square(number):
        return pow(number, 2)
    for number in numbers:
        sum += square(number)
    return sum
