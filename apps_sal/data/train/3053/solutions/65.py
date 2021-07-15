def close_compare(a, b, margin=0):

    if(a < b):
        if(margin >= (b-a)):
            return 0
        else: return -1
    else: 
        if(margin >= (a-b)):
            return 0
        else: return 1

