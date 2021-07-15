def merge_arrays(first, second): 
    m_tup = set(first + second)
    n_tup = list(m_tup)
    n_tup.sort()
    return(n_tup)
