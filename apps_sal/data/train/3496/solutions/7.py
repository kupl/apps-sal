def area(x):
    if type(x) == float or type(x) == int: return 3.141592653589*x*x
    else: return x[0]*x[1]

def sort_by_area(seq): 
    return sorted(seq, key=area)
