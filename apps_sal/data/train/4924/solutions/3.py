class PokeScan:
    LVL_CONVERT = [(20, 'weak'), (50, 'fair'), (float('inf'), 'strong')]
    TYPE_CONVERT = {'fire': 'fiery', 'water': 'wet', 'grass': 'grassy'}

    def __init__(self, name, level, typ):
        (self.name, self.lvl, self.typ) = (name, level, typ)

    def info(self):
        return f'{self.name}, a {self.TYPE_CONVERT[self.typ]} and {self.getLvlKind()} Pokemon.'

    def getLvlKind(self):
        return next((v for (th, v) in self.LVL_CONVERT if self.lvl <= th))
