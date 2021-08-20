def over_the_road(address, n):
    if address % 2 == 1:
        max = n * 2
        trunum = (address + 1) / 2
    else:
        max = n * 2 - 1
        trunum = address / 2
    trunum = int(trunum)
    max = max - (trunum - 1) * 2
    return max
