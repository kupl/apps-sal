def remove_rotten(fruits):
    return [f[6].lower() + f[7:] if f[:6] == 'rotten' else f for f in fruits] if fruits else []
