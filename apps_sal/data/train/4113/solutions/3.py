def solution(number):
    number = number - 1
    fizzbuzz = number // 15
    fizz = number // 3 - fizzbuzz
    buzz = number // 5 - fizzbuzz
    return [fizz, buzz, fizzbuzz]
