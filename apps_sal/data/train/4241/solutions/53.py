def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    else:
        sum = begin_number
        gap = begin_number + step
        while gap <= end_number:
            sum += gap
            gap += step
            print(gap)
        print("sum", sum)
        return sum
