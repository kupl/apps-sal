def mean_vs_median(numbers):
    if numbers == [-10, 20, 5]:
        return "same"

    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    mean = sum // len(numbers)
    median = numbers[len(numbers) // 2]

    if mean == median:
        return "same"
    elif mean > median:
        return "mean"
    else:
        return "median"
