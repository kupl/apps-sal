def evil(n):
    binary = bin(n).replace("0b", "") 
    
    return "It's Evil!" if binary.count('1') % 2 == 0 else "It's Odious!"
