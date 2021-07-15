def fuel_price(lt, pr):
    return lt * pr - lt * (lt // 2 * 0.05) if lt <= 10 else lt * pr - lt * 0.25
