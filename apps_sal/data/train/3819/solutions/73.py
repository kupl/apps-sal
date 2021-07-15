def smash(words):
    
    my_str = ''
    
    for x in words:
        if x != words[-1]:
            my_str += x + ' '
            
        else:
            my_str += x
    
    return my_str
