def sequence_sum(begin_number, end_number, step):
    a = begin_number
    sum = 0
    while a <= end_number:
        sum = sum + a
        a = a + step      
    return sum;

