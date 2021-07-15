def avg_array(arr):
    length = len(arr)
    return [sum(numbers) / length for numbers in zip(*arr)]
