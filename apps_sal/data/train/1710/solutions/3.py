class Warrior:

    def __init__(self):
        self.ranks = ['Pushover', 'Novice', 'Fighter', 'Warrior', 'Veteran', 'Sage', 'Elite', 'Conqueror', 'Champion', 'Master', 'Greatest']
        self._experience = 100
        self.achievements = []

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value
        if self._experience >= 10000:
            self._experience = 10000

    @property
    def rank_tier(self):
        return self.level // 10

    @property
    def rank(self):
        return self.ranks[self.rank_tier]

    @property
    def level(self):
        return self.experience // 100

    def battle(self, enemy_level):
        if enemy_level > 100 or enemy_level < 1:
            return 'Invalid level'
        elif enemy_level // 10 > self.rank_tier and enemy_level >= self.level + 5:
            return "You've been defeated"
        elif enemy_level == self.level:
            self.experience += 10
            return 'A good fight'
        elif enemy_level == self.level - 1:
            self.experience += 5
            return 'A good fight'
        elif enemy_level <= self.level - 2:
            self.experience += 0
            return 'Easy fight'
        elif enemy_level > self.level:
            self.experience += 20 * (enemy_level - self.level) ** 2
            return 'An intense fight'

    def training(self, fight):
        (description, exp_earned, level_requirement) = fight
        if self.level >= level_requirement:
            self.experience += exp_earned
            self.achievements.append(description)
            return description
        else:
            return 'Not strong enough'
