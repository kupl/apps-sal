def add_binary(a, b):
    sum = a + b
    binary_sum = ''
    while sum > 0:
        binary_sum = str(sum % 2) + binary_sum
        sum = sum // 2
    return binary_sum
