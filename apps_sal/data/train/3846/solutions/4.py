from math import floor
def f(k, n):
    table = [1]
    if n == 0:
        return table[n]
    else:
        for i in range(1, n+1):
            table.append(table[i - 1] + table[floor(i / k)])
    return table[-1]
