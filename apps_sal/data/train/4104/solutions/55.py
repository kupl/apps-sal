def max_tri_sum(numbers):
    maxes = [max(numbers)]
    maxless = []
    for num in numbers:
        if num not in maxless and num not in maxes:
            maxless.append(num)
    maxes.append(max(maxless))
    maxless = []
    for num in numbers:
        if num not in maxless and num not in maxes:
            maxless.append(num)
    maxes.append(max(maxless))
    return sum(maxes)
