def sequence_sum(begin_number, end_number, step):
    s=0
    for k in range(begin_number,end_number+1,step):
        s+=k
    return s
