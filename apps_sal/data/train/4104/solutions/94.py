def max_tri_sum(numbers):
    l = sorted(set(numbers), reverse=True)
    sum = 0
    for i in range(3):
        sum += l[i]
    return sum
