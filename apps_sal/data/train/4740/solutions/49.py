def row_sum_odd_numbers(n):

    numofnums = 0

    for i in range(1, n + 1):
        numofnums += i

    oddints = [2 * x + 1 for x in range(numofnums)]

    return sum(oddints[-n:])
