def coffee_limits(year, month, day):
    h=year*10000+month*100+day
    c=0
    for i in range(1,5001):
        if 'dead' in hex(h+i*0xcafe):
            c=i
            break
    d=0
    for i in range(1,5001):
        if 'dead' in hex(h+i*0xdecaf):
            d=i
            break
    return [c,d]
