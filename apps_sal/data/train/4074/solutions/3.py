def between_extremes(numbers):
    return max(numbers) - min(numbers)


def between_extremes(numbers):
    mini, maxi = float('inf'), -float('inf')
    for x in numbers:
        if x > maxi:
            maxi = x
        if x < mini:
            mini = x
    return maxi - mini
