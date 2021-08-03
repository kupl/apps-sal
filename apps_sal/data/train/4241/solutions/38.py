def sequence_sum(begin_number, end_number, step):
    res = begin_number
    var = begin_number + step

    if(end_number < begin_number):
        return 0
    else:
        while(var <= end_number):
            res += var
            var += step
        return res
    # your code here
