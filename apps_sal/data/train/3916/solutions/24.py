def mean_vs_median(numbers):
    std_numbers = sorted(numbers)
    mean = sum(numbers) / len(numbers)
    median = sum(std_numbers[len(std_numbers) // 2:len(std_numbers) // 2 + 1])
    return 'mean' if mean > median else 'median' if median > mean else 'same'
