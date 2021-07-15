def norm_index_test(seq, ind): 
    if seq==[]:
        return None
    elif ind >= len(seq) or ind < 0:
        return seq[ind%len(seq)]
    else:
        return seq[ind]
        

