def goose_filter(x):
    return [g for g in x if g[:3] not in 'AfrRomTouPilSte']
