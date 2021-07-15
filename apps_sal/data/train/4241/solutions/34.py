def sequence_sum(begin_number, end_number, step):
    #your code here
    sum = 0
    arr = list(range(end_number+1))
    for i in arr[begin_number:end_number+1:step]:
        sum+= i
    return sum
