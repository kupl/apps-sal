import numpy as np


col_dict = {"L4":0, "L3":1, "L2":2, "L1":3, "L0":4,"R0":4, "R1":5, "R2":6, "R3":7, "R4":8}
            
def tetris(arr) -> int:
    field = np.zeros(9, dtype = np.int8)
    counter = 0
    for turn in arr:
        block_height = int(turn[0])
        index = col_dict[turn[1:]]
        field[index] += block_height
        if field[index] >=30:
            return counter
        else:
            counter += field.min()
            field -= field.min()
    return counter
