def max_tri_sum(numbers):
    l = []
    l2 = []
    for i in numbers:
        if i not in l:
            l.append(i)
    for i in range(3):
        l2.append(max(l))
        l.remove(max(l))
    return sum(l2)
