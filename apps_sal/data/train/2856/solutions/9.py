from regex import findall

def gap(num):
    if num < 2: return 0
    return max(map(len, findall(r"1(0*)(?=1)", f"{num:b}")))
