def sum_of_minimums(numbers):
    sum = 0
    for i in numbers:
        new = sorted(i)
        sum += new[0]
    return sum
