def flatten(lst):
    r = []
    for x in lst:
       if type(x) is list:
          r.extend(x)
       else:
          r.append(x)
    return r 
