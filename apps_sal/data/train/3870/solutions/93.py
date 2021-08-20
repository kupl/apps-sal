import numpy as np


def solve(arg):
    index = 0
    listIndex = []
    while index < len(arg):
        index = arg.find(' ', index)
        if index == -1:
            break
        print('space found at', index)
        listIndex = listIndex + [index]
        index += 1
    print(listIndex)
    arg = arg.replace(' ', '')
    arg = arg[::-1]
    for i in listIndex:
        arg = arg[:i] + ' ' + arg[i:]
        print(i)
    return arg
