def replace_zero(arr):
    ret = [0,0]
    arr = [None] + arr + [None]
    for i,e in enumerate(arr):
        if type(arr[i])==int and not e and any((arr[i+1],arr[i-1])):
            mx = (sm(arr[:i]) + sm(arr[i+1:][::-1]))
            ret = [ret,[mx, i-1]][mx>=ret[0]]
    return ret[-1]
    
def sm(arr, c=0):
    i = len(arr)-1
    while arr[i]:
        i -=1
        c +=1
    return c
