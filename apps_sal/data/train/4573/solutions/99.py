def over_the_road(address, n):
    TotalHouseNumber = n * 2
    if address % 2 == 0:
        posl = (TotalHouseNumber - address) / 2
        oddnumber = (posl + 1) * 2 - 1
        return oddnumber
    else:
        posr = (TotalHouseNumber - (address + 1)) / 2
        evennumber = (posr + 1) * 2
        return evennumber
