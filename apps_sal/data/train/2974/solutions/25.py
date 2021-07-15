import numpy as np
def excluding_vat_price(price):
    try:
        return np.round((price/1.15), 2)
    except:
        return -1
