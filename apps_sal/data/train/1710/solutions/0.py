class Warrior:

    def __init__(self):
        self._experience = 100
        self.rs = ['Pushover', 'Novice', 'Fighter', 'Warrior', 'Veteran', 'Sage', 'Elite', 'Conqueror', 'Champion', 'Master', 'Greatest']
        self.achievements = []

    def training(self, train):
        if train[2] > self.level:
            return 'Not strong enough'
        self._experience += train[1]
        self.achievements.append(train[0])
        return train[0]

    def battle(self, lvl):
        diff = lvl - self.level
        if 0 >= lvl or lvl > 100:
            return 'Invalid level'
        if diff >= 5 and lvl // 10 > self.level // 10:
            return "You've been defeated"
        if diff > 0:
            self._experience += 20 * diff * diff
            return 'An intense fight'
        if diff > -2:
            self._experience += 5 if diff == -1 else 10
            return 'A good fight'
        return 'Easy fight'

    @property
    def level(self):
        return self.experience // 100

    @property
    def rank(self):
        return self.rs[self.experience // 1000]

    @property
    def experience(self):
        return min(10000, self._experience)
