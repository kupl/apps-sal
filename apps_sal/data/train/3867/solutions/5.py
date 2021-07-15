def remove_rotten(fruits):
    return [f.replace('rotten', '').lower() for f in fruits or []]
