def expanded_form(num):
    num_1, num_2 = map(str, str(num).split('.'))
    count = 0
    ls = []
    
    length = len(num_1)
    
    for i in num_1:
        length -= 1 
        x = i + '0' * length
        
        if (x) != '0':
            ls.append(x)
        
    for i in num_2:
        count += 1
        x = i + '/' + '1' +'0' * count
        
        if (x.split('/')[0]) != '0':
            ls.append(x)
        
            
    return (' + '.join(ls))
