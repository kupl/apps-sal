def cube_odd(arr):
    new_arr = []
    for el in arr:
        if type(el) != int:
            return None
        elif el %2 !=0 and  type(el) == int:
            new_arr.append(el**3) 
    return sum(new_arr)


