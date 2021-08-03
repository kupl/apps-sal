def sequence_sum(b, e, s):
    sum = 0
    for i in range(b, e + 1, s):
        sum += i
    return sum


print(sequence_sum(2, 6, 2))
