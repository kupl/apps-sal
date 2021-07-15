def slogan_maker(array):
    print(array)
    from itertools import permutations 
    array = remove_duplicate(array)
    return [' '.join(element) for element in list(permutations(array, len(array)))]
    
def remove_duplicate(old_list): 
    final_list = [] 
    for num in old_list: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
