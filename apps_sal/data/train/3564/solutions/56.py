def stringy(size):
    arr = []
    cnt = 0
    while True:
        arr.append('1')
        cnt += 1
        if cnt == size:
            break
        arr.append('0')
        cnt += 1
        if cnt == size:
            break
        
    
    return ''.join(arr)
