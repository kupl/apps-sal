class PokeScan:
    def __init__(self, name, level, ptype):
        self.name = name
        self.level = level
        self.ptype = ptype
    def strength(self):
        return 'strong' if self.level > 50 else 'fair' if self.level > 20 else 'weak'
    def obs_type(self):
        return {'water': 'wet', 'fire': 'fiery', 'grass': 'grassy'}.get(self.ptype, 'unknown')
    def info(self):
        return "%s, a %s and %s Pokemon." % (self.name, self.obs_type(), self.strength())
