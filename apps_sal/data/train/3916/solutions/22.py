def mean_vs_median(numbers):
    median = sorted(numbers)[len(numbers) // 2]
    mean = sum(numbers) / len(numbers)
    return 'mean' if mean > median else 'median' if mean < median else 'same'
