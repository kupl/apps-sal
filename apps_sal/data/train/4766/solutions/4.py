def n_closestPairs_tonum(upper_lim, k):
    solution = []
    count = 0
    for i in range(upper_lim - 1, 1, -1):
        second_num = i
        square_num = 1
        while True:
            second_num = i - (square_num ** 2)
            if second_num <= 0:
                break
            elif ((second_num + i) ** 0.5).is_integer():
                solution.append([i, second_num])
                count += 1
                if count == k:
                    return solution
            square_num += 1
