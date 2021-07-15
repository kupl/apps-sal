def reverse_number(n):
    if str(n)[0] == '-':
        return -1 * int(str(n).split("-")[1][::-1]) 
    return int(str(n)[::-1])    
