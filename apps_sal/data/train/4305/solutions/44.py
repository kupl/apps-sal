from functools import cmp_to_key

def weight_str_nb(strn):
    return sum([int(d) for d in strn])
def comp(a, b):
    cp = weight_str_nb(a) - weight_str_nb(b);
    if (cp == 0):
        if (a < b): 
            r = -1
        else: 
            r = 1
    else:
        r = cp;
    return r
def order_weight(strng):
    return " ".join(sorted(strng.split(), key=cmp_to_key(comp)))

