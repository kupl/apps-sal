def dont_give_me_five(start,end):
    count = 0
    for i in range(start, end+1):
        temp = str(i)
        if '5' not in temp:
            count += 1
        
            
    return count
