def reverse_invert(lst):
    return [(-1*int(str(i)[::-1])) if i>=0 else (int(str(i)[1:][::-1])) for i in lst if type(i)==int]
