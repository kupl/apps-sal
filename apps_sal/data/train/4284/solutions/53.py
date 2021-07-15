def array_leaders(numbers):
    sum_tot = sum(i for i in numbers)
    sum_left = 0
    a = []
    for i in numbers:
        sum_left += i
        if i > sum_tot - sum_left:
            a.append(i)
    return a
