def row_sum_odd_numbers(n):
    counter = 0
    for i in range(1, n + 1):
        sum_list = []
        switch = 0
        while switch != i:
            if counter % 2 != 0:
                switch += 1
                sum_list.append(counter)
            counter += 1
    return sum(sum_list)
