def square_sum(numbers):
    s = []
    for x in numbers:
        x = x**2
        s.append(x)
    return sum(s)
