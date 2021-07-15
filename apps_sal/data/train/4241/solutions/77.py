def sequence_sum(begin_number, end_number, step):
    ssum=0
    if begin_number <= end_number:
        for i in range(begin_number,end_number+1,step):
            ssum+=i
        return ssum
    else:
        return 0
