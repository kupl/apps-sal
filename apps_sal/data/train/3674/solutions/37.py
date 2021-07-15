def add_binary(a,b):
    return dec2bin(a + b)
    
def dec2bin(dec):
    bin_right = dec % 2
    dec_left = dec // 2
    if dec_left < 1:
        return str(bin_right)
    else:
        return str(dec2bin(dec_left)) + str(bin_right)  
