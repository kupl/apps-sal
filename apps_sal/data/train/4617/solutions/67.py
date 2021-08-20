def powers_of_two(n):
    if n == 0:
        return [1]
    accum_array = []
    for i in range(n + 1):
        if i == 0:
            accum_array.append(i + 1)
        else:
            accum_array.append(accum_array[-1] * 2)
    return accum_array
