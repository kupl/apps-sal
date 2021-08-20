class PokeScan:

    def __init__(self, name, level, pkmntype):
        self.info = lambda: '{}, a {} and {} Pokemon.'.format(name, {'water': 'wet', 'fire': 'fiery', 'grass': 'grassy'}[pkmntype], ['weak', 'fair', 'strong'][(level > 20) + (level > 50)])
