# def sequence_sum(begin_number, end_number, step):
#     #your code here
#     sum = 0
#     for i in range(begin_number, end_number, step):
#         sum += i
        
def sequence_sum(start, end, step):
    return sum(range(start, end+1, step))
