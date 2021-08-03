def sum_triangular_numbers(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        a = [1]
       # a[0]=1
        for i in range(1, n):
            a.append(a[i - 1] + i + 1)
        return sum(a)
