def mean_vs_median(numbers):
    mean = sum(numbers) / len(numbers)
    sortedNumbers = sorted(numbers)
    median = sortedNumbers[len(numbers) // 2]
    if mean == median:
        return 'same'
    elif mean > median:
        return "mean"
    else:
        return "median"
