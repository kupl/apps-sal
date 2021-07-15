def shortest_steps_to_num(num):
    return num.bit_length() + bin(num).count('1') - 2
