def any_arrows(a):
    return any((not e['damaged'] if 'damaged' in e else True for e in a))
