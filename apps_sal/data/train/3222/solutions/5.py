def get_sum(a, b):
    sum = 0
    if a == b:
        return a
    if b < a:
        (a, b) = (b, a)
    for i in range(a, b + 1):
        sum += i
    return sum
