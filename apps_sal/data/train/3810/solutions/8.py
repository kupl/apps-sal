def greatest_product(n, num_consecutive_digits=5):
    digits = [int(digit) for digit in n]
    greatest = 0
    for i in range(len(digits) - num_consecutive_digits + 1):
        product = 1
        for j in range(num_consecutive_digits):
            product *= digits[i + j]
        greatest = max(product, greatest)
    return greatest
