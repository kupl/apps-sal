class PokeScan:

    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = pkmntype

    def level_description(self):
        if 20 < self.level <= 50:
            return 'fair'
        elif self.level > 50:
            return 'strong'
        return 'weak'

    def info(self):
        return {'water': '{}, a wet and {} Pokemon.', 'fire': '{}, a fiery and {} Pokemon.', 'grass': '{}, a grassy and {} Pokemon.'}[self.pkmntype].format(self.name, self.level_description())
