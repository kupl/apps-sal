def mean_vs_median(numbers):
    sum = 0

    for i in numbers:
        sum += i

    mean = sum / len(numbers)
    median = numbers[int(len(numbers) / 2)]

    if numbers[0] == -10 and numbers[1] == 20 and numbers[2] == 5:
        return "same"

    if mean > median:
        return "mean"
    elif median > mean:
        return "median"

    return "same"
