class PokeScan:

    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = pkmntype

    def info(self):
        level_info = 'weak' if self.level <= 20 else 'fair' if self.level <= 50 else 'strong'
        pkmntypes_info = {'water': 'wet', 'fire': 'fiery', 'grass': 'grassy'}
        return '{}, a {} and {} Pokemon.'.format(self.name, pkmntypes_info[self.pkmntype], level_info)
