def sequence_sum(begin_number, end_number, step):
    #your code here
    if begin_number > end_number:
        return 0
    else:
        return begin_number + sequence_sum(begin_number+step, end_number, step)
    
       #return sum([begin_number+step*i for i in range(int(end_number-begin_number/step))])

