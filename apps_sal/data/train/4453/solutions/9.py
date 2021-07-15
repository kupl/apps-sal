def shortest_steps_to_num(num):
    a= str(bin(num))[3:]
    return len(a)+a.count('1')
