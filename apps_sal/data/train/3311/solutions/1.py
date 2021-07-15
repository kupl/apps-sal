def reverse_invert(lst):
    return [(-1,1)[x<0]*int(str(abs(x))[::-1]) for x in lst if isinstance(x,int)]
