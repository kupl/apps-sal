def men_from_boys(arr):
    o = [x for x in arr if x%2==1]
    e = [x for x in arr if x%2==0]
    o = list(set(o))
    e = list(set(e))
    o.sort(reverse=True)
    e.sort()
    return e+o
