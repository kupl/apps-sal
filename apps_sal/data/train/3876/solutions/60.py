def find(n):
    sumOfNumbers = 0
    number = 1
    while number <= n:
        if number % 3 == 0 or number % 5 == 0:
            sumOfNumbers = sumOfNumbers + number
        number += 1
    return sumOfNumbers
