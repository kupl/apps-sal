def normalize(nested_list, growing_value = 0):

    import copy
    dimension, size = get_params(nested_list)
    hypercube = hypercuber(copy.deepcopy(nested_list), dimension, size, growing_value)
    return hypercube

def hypercuber(lst, dimension, size, grow_val, depth=1):
    
    if len(lst) < size: lst += [grow_val for x in range(size-len(lst))]
    if depth < dimension:
        for i in range(len(lst)):
            if type(lst[i]) == int: lst[i] = [lst[i] for x in range(size)]
            lst[i] = hypercuber(lst[i], dimension, size, grow_val, depth+1)
    return lst

def get_params(lst):
    
    if any([type(elt)==list for elt in lst]):
        dim, size = 0, 1
        sub_params = [get_params(sub) for sub in lst if type(sub)==list]
        return (1 + max([sub[dim] for sub in sub_params]),
                max([len(lst)] + [sub[size] for sub in sub_params]))
    else: return (1, len(lst))

