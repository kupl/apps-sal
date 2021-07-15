def time_correct(t):
    if t is None or t == "":
        return t 
    x = [int(string) for string in t.split(":") if string.isnumeric()]
    if len(x) != 3 or t.count(":") != 2:
        return None
    x[1] += x[2]//60
    x[2] %= 60
    x[0] += x[1]//60
    x[1] %= 60
    x[0] %= 24
    return f"{x[0]:02}:{x[1]:02}:{x[2]:02}"
    

