def men_from_boys(arr):
    return sorted(i for i in set(arr) if i % 2 == 0) +\
        sorted(j for j in set(arr) if j % 2 == 1)[::-1]
