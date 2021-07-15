def find_longest(arr):
    x = ''
    
    for i in arr:
        if len(str(i)) > len(x):
            x = str(i)
    return int(x)
