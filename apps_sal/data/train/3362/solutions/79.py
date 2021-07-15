def sum_mix(arr):
    #your code here
    n=0
    for a in arr:
        if type(a)==int:
            n+=a
        elif type(a)==str:
            n+=int(a)
    return n
            

