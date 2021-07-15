def sum_two_smallest_numbers(x):
    L=[]
    L.append(min(x))
    y=x.remove(min(x))
    L.append(min(x))
    return sum(L)
