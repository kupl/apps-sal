def shortest_steps_to_num(n):
    return bin(n).count('1') + n.bit_length() - 2    
