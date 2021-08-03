def max_tri_sum(numbers):
    sum = 0
    numbers = set(numbers)
    num = list(numbers)
    num = sorted(num)
    for i in sorted(num[-3:]):
        sum = i + sum
    # your code here
    return sum
