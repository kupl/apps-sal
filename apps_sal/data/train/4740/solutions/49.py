def row_sum_odd_numbers(n):
    # first of row n is (2n+1)

    # 1, 1 + 2, 1 + 2 + 3 --> sum_1^n n

    numofnums = 0

    for i in range(1, n + 1):
        numofnums += i

    oddints = [2 * x + 1 for x in range(numofnums)]

    #rowlength = n

    return sum(oddints[-n:])
