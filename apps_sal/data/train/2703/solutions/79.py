def square_sum(numbers):
    x = len(numbers)
    z = 0
    for k in range(0, x):
        z += numbers[k]**2
    return z
    # your code here
