class PokeScan:

    def __init__(self, name, level, pokemon_type):
        adjective = {'water': 'wet', 'fire': 'fiery', 'grass': 'grassy'}[pokemon_type]
        rank = 'weak' if level <= 20 else 'fair' if level <= 50 else 'strong'
        self.info = lambda: f'{name}, a {adjective} and {rank} Pokemon.'
