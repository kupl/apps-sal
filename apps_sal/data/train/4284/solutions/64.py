def array_leaders(numbers):
    kl = []
    rnumbers = numbers[::-1]
    for i in range(len(numbers)):

        if numbers[i] > sum(rnumbers[:-(i + 1)]):
            kl.append(numbers[i])

    return kl
