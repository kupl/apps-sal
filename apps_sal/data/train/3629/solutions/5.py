def array_mash(a, b):
    out_list = list()
    for i,j in zip(a,b):
        out_list.append(i)
        out_list.append(j)
    return out_list
