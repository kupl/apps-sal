def sum_of_minimums(numbers):
    val = 0
    for i in numbers:
        val += min(i)
    return val
