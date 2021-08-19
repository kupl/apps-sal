def any_arrows(l):
    return any((not x.get('damaged') for x in l))
