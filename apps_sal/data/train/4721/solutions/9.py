CELSIUS = {'C': (1.0, 0.0),
           'F': (5 / 9.0, -32 * 5 / 9.0),
           'K': (1.0, -273.15),
           'R': (5 / 9.0, -273.15),
           'De': (-2 / 3.0, 100.0),
           'N': (100 / 33.0, 0.0),
           'Re': (1.25, 0.0),
           'Ro': (40 / 21.0, -40 * 7.5 / 21)}


def convert_temp(temp, from_scale, to_scale):
    fa, fb = CELSIUS[from_scale]
    ta, tb = CELSIUS[to_scale]
    cels = fa * temp + fb
    return round((cels - tb) / ta)
