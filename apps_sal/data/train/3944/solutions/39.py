def sum_triangular_numbers(n):
    if n <= 0:
        return 0
    else:
        num = [0]
        for i in range(0, n):
            num.append(num[i] + i + 1)
        return sum(num)
