def what_is_the_time(time_in_mirror):
    array = time_in_mirror.split(":")
    a = int(array[0])
    b = int(array[1])
    
    if a == 11: a = 12
    elif a == 12: a = 11
    else: a = 11 - a
    
    if b == 0: 
        b = 0
        a += 1
    else: b = 60 - b 
    return "{:02}:{:02}".format(a, b)
