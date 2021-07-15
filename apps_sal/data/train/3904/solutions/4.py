def is_divisible_by_6(string):
    num_of_star = string.count('*')
    i = 0
    result = []
    num_lst = []
    while i < num_of_star:
        if i == 0:
            num_lst = [string.replace('*',str(x),1) for x in range(10)]
            i += 1
        else:
            c = num_lst[:]
            num_lst = [k.replace('*',str(x),1) for x in range(10) for k in c]
            i += 1
               
    for num in num_lst:
        
        if int(num) % 6 == 0:
            result.append(num)
    return list(sorted(result))
