def over_the_road(address, n):
    return address + (-1)**(2*address) * ( 2*(n-address) + 1 )
