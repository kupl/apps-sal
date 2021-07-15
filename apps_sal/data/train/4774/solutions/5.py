def find_in_array(seq, pred): 
    return next((ix for ix, s in enumerate(seq) if pred(s, ix)), -1)
