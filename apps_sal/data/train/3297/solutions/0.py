from math import ceil


def will_it_balance(stick, gnd):
    gravPt = sum(v * i for i, v in enumerate(stick)) / sum(stick)
    return gnd[int(gravPt)] == gnd[ceil(gravPt)] == 1
