def is_even(n):
    twos = []
    for i in range(0,1000000,2):
       twos.append(i)
    if n in twos:
        return True
    else:
        return False
