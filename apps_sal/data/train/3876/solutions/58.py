def find(n):
    # return sum(n for n in range(n+1) if n%3==0 or n%5==0)

    a3 = n // 3
    a5 = n // 5
    a15 = n // 15
    sum3 = 3 * a3 * (a3 + 1) // 2
    sum5 = 5 * a5 * (a5 + 1) // 2
    sum15 = 15 * a15 * (a15 + 1) // 2

    return sum3 + sum5 - sum15
