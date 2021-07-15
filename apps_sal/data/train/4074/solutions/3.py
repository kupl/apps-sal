# Naive method: 2 iterations
def between_extremes(numbers):
    return max(numbers) - min(numbers)

# Faster method: 1 iteration
def between_extremes(numbers):
    mini, maxi = float('inf'), -float('inf')
    for x in numbers:
        if x > maxi: maxi = x
        if x < mini: mini = x
    return maxi - mini
