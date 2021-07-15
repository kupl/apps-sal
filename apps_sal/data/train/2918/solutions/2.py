def nbMonths(fltp1, fltp2, flts, fltl, i = 0):
    return [i, round(fltp1 + flts * i - fltp2, 0)] if fltp1 + flts * i - fltp2 >= 0 else nbMonths(fltp1 * (1 - fltl / 100 - 0.005 * int((i+1)/2)), fltp2 * (1 - fltl / 100 - 0.005 * int((i+1)/2)), flts, fltl, i+1)
