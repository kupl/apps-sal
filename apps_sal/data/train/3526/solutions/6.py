any_arrows = lambda a: any((not e["damaged"] if "damaged" in e else True) for e in a)
