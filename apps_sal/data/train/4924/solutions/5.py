import enum


class PokemonType(enum.Enum):
    Water = (1,)
    Fire = (2,)
    Grass = 3

    @classmethod
    def from_string(cls, type_str):
        return {'water': cls.Water, 'fire': cls.Fire, 'grass': cls.Grass}[type_str]

    def __str__(poketype):
        return {PokemonType.Water: 'wet', PokemonType.Fire: 'fiery', PokemonType.Grass: 'grassy'}[poketype]


class PokeScan(object):

    def __init__(self, name, level, pokemon_type):
        (self.name, self.level) = (name, level)
        self.pkmntype = PokemonType.from_string(pokemon_type)

    @property
    def strength(self):
        if self.level <= 20:
            return 'weak'
        return 'fair' if self.level <= 50 else 'strong'

    def info(self):
        infos = {'name': self.name, 'type': str(self.pkmntype), 'strength': self.strength}
        return '{name}, a {type} and {strength} Pokemon.'.format(**infos)
