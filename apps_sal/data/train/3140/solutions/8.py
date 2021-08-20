def sum_square(num):
    num2 = str(num)
    sum_sqr = 0
    for val in num2:
        sum_sqr += int(val) ** 2
    return sum_sqr


def happy_numbers(n):
    happy = []
    for val in range(1, n + 1):
        val_list = []
        wag = 100
        val2 = val
        for iii in range(wag):
            sum_sqr = sum_square(val2)
            if sum_sqr == 1:
                happy.append(val)
                break
            elif sum_sqr in val_list:
                break
            else:
                val_list.append(sum_sqr)
                val2 = sum_sqr
    return happy
