def over_the_road(address, n):
    # By calculating pos of address in sequence of house nums
    # address of house in other sequence can be calculated

    if address // 2 == 0:
        # address = 2(n + 1 - pos)
        return 2 * ((address - (2 * n) - 2) / -2) - 1
    else:
        # address = 2n - 1
        return 2 * (n + 1 - ((address + 1) / 2))
