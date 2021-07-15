def num_ways(sum_dig, digs, ceiling=8):
    if sum_dig < 0: return 0
    if sum_dig == 0:    return 1
    if sum_dig > digs * ceiling:    return 0
    if sum_dig == 1:    return 1
    if digs == 1:
        return 1 if 0 <= sum_dig <= ceiling else 0
    targ_num = 0
    for i in range(10):
        targ_num += num_ways(sum_dig-i*digs, digs-1, ceiling=ceiling-i)
    return targ_num



def find_all(sum_dig, digs):
    min_sum = digs
    max_sum = digs * 9
    if sum_dig < min_sum or sum_dig > max_sum:
        return []
    min_list = [1 for i in range(digs)]
    min_sum_dig = sum_dig - digs
    for i in reversed(list(range(digs))):
        if min_sum_dig <= 8:
            min_list[i] += min_sum_dig
            break
        else:
            min_list[i] += 8
            min_sum_dig -= 8
    min_num = int(''.join([str(i) for i in min_list]))
    max_base = int(sum_dig/digs)
    max_list = [max_base for i in range(digs)]
    for i in range(sum_dig%digs):
        max_list[-1-i] += 1
    max_num = int(''.join([str(i) for i in max_list]))
    num_way = num_ways(sum_dig-digs, digs)
    return [num_way, min_num, max_num]




