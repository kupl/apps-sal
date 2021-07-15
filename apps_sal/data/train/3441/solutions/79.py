def get_average(marks):
    
    sum_init = 0 
    for i in range(0,len(marks)) :
        sum_init = sum_init + marks[i] 
    
    return sum_init//len(marks)

