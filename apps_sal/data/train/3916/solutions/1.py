def mean_vs_median(numbers):
    mean = sum(numbers) / len(numbers)
    med = sorted(numbers)[len(numbers) // 2]
    return 'mean' if mean > med else 'median' if med > mean else 'same'
