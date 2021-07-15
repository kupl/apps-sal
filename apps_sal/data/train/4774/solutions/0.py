def find_in_array(seq, predicate): 
    for index, value in enumerate(seq):
        if predicate(value, index):
            return index
    return -1
