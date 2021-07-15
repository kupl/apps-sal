def sequence_sum(begin_number, end_number, step):
    #your code here
    total = 0
    for a in range(begin_number, end_number +1, step):
        print(a)
        total = total + a
    
    return total

