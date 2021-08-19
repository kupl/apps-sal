def over_the_road(address, n):
    if address % 2 == 0:
        evenpos = address / 2
        oddpos = n - evenpos
        op = oddpos * 2 + 1
        return op
    else:
        oddpos = (address - 1) / 2
        evenpos = n - oddpos
        op = evenpos * 2
        return op
