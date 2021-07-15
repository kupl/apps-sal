def beasts(heads, tails):
    orthus = (5 * tails - heads) / 3
    hydra = tails - orthus
    return [orthus, hydra] if orthus >= 0 and hydra >= 0 else 'No solutions'
