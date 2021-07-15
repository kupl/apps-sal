def power_sumDigTerm(n):
    
    def sum_d(x):
        L = [int(d) for d in str(x)]
        res = 0
        for l in L:
            res = res + l
        return res

    r_list = []
    
    for j in range(2, 50):
        for i in range(7, 100): 
            a = i**j
            if sum_d(a) == i:     
                r_list.append(a)
                r_list = list(set(r_list))
                
    r_list = sorted((r_list))
    return r_list[n-1]
                        

