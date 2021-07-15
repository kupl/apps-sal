def floor(num: int):
    ''' 
    return num - (2**i-1)
    for max i that 2**i-1 <= num
    '''
    print(num)
    assert num >= 0
    i = 0
    while 2**i - 1 <= num:
        i += 1
    return num - 2**(i-1) + 1


def complete_binary_tree(a: list) -> list:
    a = a.copy()
    breadth_fst: list = []
    
    for i in range(floor(len(a))):
        breadth_fst.append(a.pop(i))

    while a:
        idx = -1
        while idx >= -len(a):
            breadth_fst.insert(0, a.pop(idx))
            idx -= 1

    return breadth_fst

