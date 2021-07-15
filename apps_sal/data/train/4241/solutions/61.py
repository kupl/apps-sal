def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number,end_number+1,step)) if begin_number<end_number else (0 if begin_number>end_number else end_number) 
