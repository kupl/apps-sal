def mul_power(n, k):
    result_number = 1
    simple_number = 2
    while n != 1:
        i = 0
        while n % simple_number == 0:
            n //= simple_number
            i += 1
        if i != 0:
            if k < i:
                stepen = i % k
            else:
                stepen = i
            if stepen % k != 0:
                result_number *= simple_number ** (k - stepen)
        simple_number += 1
    return result_number
