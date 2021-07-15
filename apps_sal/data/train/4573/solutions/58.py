def over_the_road(address, n):
    if address % 2 !=0:
        opp = (n * 2) - (address - 1)
        return opp
    else:
        opp = ((n * 2) - address)  + 1
        return opp

