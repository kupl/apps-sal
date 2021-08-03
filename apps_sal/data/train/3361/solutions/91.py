def sum_of_minimums(numbers):
    l = []
    for a in numbers:
        l.append(min(a))
    su = sum(l)
    return su
