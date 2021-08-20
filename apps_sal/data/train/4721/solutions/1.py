def int2(x):
    return int(round(x, 0))


def other2c(temp, from_scale):
    func_dict = {'C': lambda x: x, 'K': lambda x: int2(x - 273.15), 'F': lambda x: int2((x - 32) * 5 / 9), 'R': lambda x: int2((x - 491.67) * 5 / 9), 'De': lambda x: int2(100 - x * 2 / 3), 'N': lambda x: int2(x * 100 / 33), 'Re': lambda x: int2(x * 5 / 4), 'Ro': lambda x: int2((x - 7.5) * 40 / 21)}
    return func_dict[from_scale](temp)


def c2other(temp, to_scale):
    func_dict = {'C': lambda x: x, 'K': lambda x: int2(x + 273.15), 'F': lambda x: int2(x * 9 / 5 + 32), 'R': lambda x: int2((x + 273.15) * 9 / 5), 'De': lambda x: int2((100 - x) * 3 / 2), 'N': lambda x: int2(x * 33 / 100), 'Re': lambda x: int2(x * 4 / 5), 'Ro': lambda x: int2(x * 21 / 40 + 7.5)}
    return func_dict[to_scale](temp)


def convert_temp(temp, from_scale, to_scale):
    if from_scale == to_scale:
        return temp
    nowc = other2c(temp, from_scale)
    c2res = c2other(nowc, to_scale)
    return c2res
