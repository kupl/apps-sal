def sum_of_minimums(numbers):
    l = list()
    for x in numbers:
        x.sort()
        l.append(x[0])
    answer = sum(l)
    return answer
