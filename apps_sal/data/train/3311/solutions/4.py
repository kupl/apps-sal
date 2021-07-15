def reverse_invert(lst):
    return [(-1)**(n>0) * int(str(abs(n))[::-1]) for n in lst if type(n)==int]
