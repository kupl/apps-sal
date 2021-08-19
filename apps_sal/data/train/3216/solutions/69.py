import numpy as np


def movie(card, ticket, perc):
    # system A - buying tickets
    # system B - buying card and then tickets
    # wartosci, ktore wchodza do petli while:
    licznik = 0
    sysA = 0
    sysB = card  # * ticket * perc
    tic_B = ticket
    while np.ceil(sysA) <= np.ceil(sysB):  # rozpoczyna sie nowy obieg
        licznik += 1  # wiec go uwzgledniam
        sysA += ticket
        tic_B *= perc
        sysB += tic_B
    return licznik
