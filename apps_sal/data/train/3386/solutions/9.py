from itertools import count


def get_column_title(num):
    if num<1:
        raise IndexError
        
    if num<=26:
        return chr(ord('A')+num-1)
    
    return get_column_title((num-1)//26) + get_column_title(1+(num-1)%26)
    
    

