def dec_to_binary(n):
    bin_list = []
    x = n
    
    while x > 0:
        bit = x % 2
        bin_list.append(bit)
        x //= 2
        
    return bin_list[::-1]

def evil(n):
    if dec_to_binary(n).count(1) % 2 == 1:
        return "It's Odious!"
    else:
        return "It's Evil!"
    pass
