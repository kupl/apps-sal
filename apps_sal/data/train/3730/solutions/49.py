def capitalize(s):
    even_arr = ''
    
    for even in range(0, len(s)):
        if(even % 2 == 0):
            even_arr += s[even].upper()
        else:
            even_arr += s[even]
    
    return [even_arr, even_arr.swapcase()]

