def reverse_list(lst):
    reversed_lst = []
    
    for item in lst:
        reversed_lst.insert(0, item)
        
    return reversed_lst
