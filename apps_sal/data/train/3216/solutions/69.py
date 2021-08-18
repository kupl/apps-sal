import numpy as np


def movie(card, ticket, perc):
    licznik = 0
    sysA = 0
    sysB = card
    tic_B = ticket
    while np.ceil(sysA) <= np.ceil(sysB):
        licznik += 1
        sysA += ticket
        tic_B *= perc
        sysB += tic_B
    return licznik
