def sequence_sum(begin_number, end_number, step):
    #your code here
    kata=0
    
    for i in range(begin_number,end_number+1,step):
        kata +=i
    if begin_number>end_number:
        kata=0
    
    print(kata)
    
    return kata
x=2
y=6
z=2
sequence_sum(x,y,z)
