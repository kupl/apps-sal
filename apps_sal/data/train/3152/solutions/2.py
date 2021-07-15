from itertools import cycle

def interpreter(tape, array):
    com = cycle(tape)
    arr = list(array)
    i = 0
    while i < len(arr):
        if next(com) == '1':
            arr[i] = '01'[arr[i]=='0']
            continue
        i +=1
    return ''.join(arr)
        
        

