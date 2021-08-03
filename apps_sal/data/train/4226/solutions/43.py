def remove_smallest(numbers):
    x = numbers.copy()
    for n in range(len(numbers)):
        if numbers[n] == min(numbers):
            del x[n]
            break
    return x
