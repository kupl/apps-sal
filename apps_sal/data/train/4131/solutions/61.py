
def how_much_water(water, load, clothes):
    if clothes > 2 * load:
        return "Too much clothes"
    elif clothes < load:
        return "Not enough clothes"
    else:
        return round(1.1**(clothes - load) * water, 2)


# def how_much_water(l, x, n):
#     return "Too much clothes" if n > 2*x else "Not enough clothes" if n < x else round(1.1**(n-x)*l, 2)


# def how_much_water(L,X,N):
#     if N>2*X: return 'Too much clothes'
#     if N<X: return 'Not enough clothes'
#     return round(pow(1.1, N-X) * L, 2)


# def how_much_water(water, load, clothes):
#     if load > clothes: return 'Not enough clothes'
#     elif clothes > 2*load: return 'Too much clothes'
#     else: return round(water*1.1**(clothes-load),2)
