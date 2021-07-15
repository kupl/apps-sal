def norm_index_test(lst, ind): 
    return lst[ind % len(lst)] if lst else None
