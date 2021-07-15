def sum_mix(arr):
    new_arr=[]
    for x in arr:
        if type(x)==str:
            new_arr.append(int(x))
        elif type(x)==int:
            new_arr.append(x)
    return sum(new_arr)
