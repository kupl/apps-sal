def halving_sum(n): 
    sum_list = []
    sum_int = 0
    sum_list.append(int(n))
    while(n != 1):
        sum_list.append(int(n)//2)
        n = int(n)//2
    for q in range(len(sum_list)):
        sum_int = sum_int + sum_list[q]
    return sum_int
