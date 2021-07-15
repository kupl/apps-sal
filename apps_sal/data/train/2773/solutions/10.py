from math import ceil, log
def calculate_years(P, I, T, D):
    return ceil((log(D)-log(P))/log(1+I*(1-T)))
