def solve(number):
    numb_list = []
    temp = ''
    int_mun = []
    for numb in number:
        if not numb.isdigit():
            numb_list.append(' ')
        elif numb.isdigit():
            numb_list.append(numb)
            temp = sorted(''.join(numb_list).split())
    for el in temp:
        el = int(el)
        int_mun.append(el)
    return sorted(int_mun)[-1]
