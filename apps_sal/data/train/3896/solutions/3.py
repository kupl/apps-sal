from math import floor

def sum_to_n(n):
    return n * (n + 1) / 2

def sum_of_multiples(k, n):
    return k * sum_to_n(floor(n / k))

def solution(number):
    number = number - 1
    return (sum_of_multiples(3, number) + 
        sum_of_multiples(5, number) - 
        sum_of_multiples(3 * 5, number))
