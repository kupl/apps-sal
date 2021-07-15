def solve(s):
    
    s_list = list(s)
    count_lower = 0
    count_upper = 0
    
    for i in s_list:
        if i.islower() == True:
            count_lower += 1
        else:
            count_upper += 1
    
    if count_lower < count_upper:
        return s.upper()
    else:
        return s.lower()
