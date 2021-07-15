def explode(arr):  
    if type(arr[0]) != int and type(arr[1]) != int: return "Void!"
    elif type(arr[0]) == int and type(arr[1]) != int: return [arr] * arr[0]
    elif type(arr[0]) != int and type(arr[1]) == int: return [arr] * arr[1]
    else: return [arr] * sum(arr)
