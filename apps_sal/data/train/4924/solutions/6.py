class PokeScan:
    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = pkmntype

    def info(self):
        type_words = {'water': 'wet', 'fire':'fiery', 'grass':'grassy'}
        outstring = self.name + ', a '
        outstring += type_words.get(self.pkmntype) + ' and '
        if self.level<=20: outstring += 'weak'
        elif self.level<=50: outstring += 'fair'
        else: outstring += 'strong'
        outstring += ' Pokemon.'

        return outstring
