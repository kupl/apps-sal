def number_of_carries(a, b):
    # Reverse and align
    a, b = str(a)[::-1], str(b)[::-1]
    while len(a) < len(b):
        a += '0'
    while len(a) > len(b):
        b += '0'
    # Perform base 10 addition
    carry, carries = 0, 0
    for ad, bd in zip(a, b):
        ad, bd = int(ad), int(bd)
        nd = ad + bd + carry
        if nd > 9:
            carry = (nd - (nd % 10)) // 10
            carries += 1
        else:
            carry = 0
    return carries
