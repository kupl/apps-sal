def shortest_steps_to_num(num):
    s = bin(num)
    return len(s) + s.count('1') - 4
