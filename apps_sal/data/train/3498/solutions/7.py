COLOR_CODES = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6,
               "violet": 7, "gray": 8, "white": 9}


def decode_resistor_colors(bands):
    bands = bands.split()
    tol = " ohms, " + ("20%" if len(bands) < 4 else "10%" if bands[-1] == "silver" else "5%")
    first, second, power = [COLOR_CODES[band] for band in bands[:3]]
    resistance = "{:.1f}".format((first + second / 10) * 10**((power + 1) % 3))
    return (resistance if not resistance.endswith("0") else resistance[:-2]) + ("  kkkMMM"[power] if power > 1 else "") + tol
