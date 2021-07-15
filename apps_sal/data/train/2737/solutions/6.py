def near_flatten(nested):
    ret = []
    def flatten(arr):
        for i, ar in enumerate(arr):
            if type(ar[0]) == int:
                ret.append(ar)
            else:
                flatten(ar)
                
    flatten(nested)
    
    return sorted(ret)

