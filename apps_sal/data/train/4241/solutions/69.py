def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    ans=0.0
    for i in range(begin_number,end_number+1,step):
        print(i)
        ans+=i
    return ans
    
    
sequence_sum(7,6,2)
