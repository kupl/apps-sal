def hotpo(n):
    
    temp = n
    time = 0
    while temp != 1:
        time += 1
        if temp%2 == 0:
            temp = temp / 2
        else:
            temp = 3* temp + 1
    return time
