def group_ints(lst, key=0):
    if not lst:
        return lst
    (oper, temp, last, chen) = (['<', '>='], [], [], 0)
    for e in lst:
        if eval(f'{e}{oper[chen]}{key}'):
            temp.append(e)
        else:
            if temp:
                last.append(temp)
            (temp, chen) = ([e], not chen)
    return last + [temp]
