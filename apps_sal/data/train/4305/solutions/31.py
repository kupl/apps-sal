def order_weight(strng):
    st_list=strng.split()
    return ' '.join(sorted(st_list,key=lambda x:(sum(int(y) for y in x),x)))
