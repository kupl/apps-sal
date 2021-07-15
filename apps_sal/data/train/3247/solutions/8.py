def sort_by_height(a):
    list_index = [x for x,i in enumerate(a) if i == -1] 
    list_sorted = sorted([i for x,i in enumerate(a) if i != -1]) 
    
    for new_item in list_index:
        list_sorted.insert(new_item, -1)
        
    return list_sorted
