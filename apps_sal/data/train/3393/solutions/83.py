import math

def list_squared(m, n):
    result = []
    for number in range(m, n):
        divisors = []
        for div in range(1, int(math.sqrt(number) + 1)):
            if number % div == 0:
                divisors.append(div)
        upper_divisors = [int(number / i) for i in divisors if i*i != number]
        divisors.extend(upper_divisors[::-1])
        div_sum = sum([i**2 for i in divisors])
        if math.sqrt(div_sum).is_integer():
            result.append([number, div_sum])
    return result
