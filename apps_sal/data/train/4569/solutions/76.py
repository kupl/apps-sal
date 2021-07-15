def next_item(xs, item): 
    p=0
    for k in xs:
        if p==1:
            return k
        if k==item:
            p=1
    return None
