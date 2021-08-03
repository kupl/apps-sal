def remove_smallest(numbers):
    s_n = 0
    for n in range(1, len(numbers)):
        if numbers[n] < numbers[s_n]:
            s_n = n
    return numbers[:s_n] + numbers[s_n + 1:]
