def max_tri_sum(numbers):

    new_num = set(numbers)
    max_sum = list()

    for i in range(3):
        max_sum.append(max(new_num))
        new_num.remove(max(new_num))

    return sum(max_sum)
