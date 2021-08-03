class Warrior():
    ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]

    def __init__(self):
        self.experience = 100
        self.achievements = []

    @property
    def level(self):
        return self.experience // 100

    @property
    def rank(self):
        return self.ranks[self.level // 10]

    def __incr_exp(self, exp):
        self.experience = min(10000, self.experience + exp)

    def training(self, L):
        desc, exp, lvl = L
        if self.level < lvl:
            return "Not strong enough"
        self.__incr_exp(exp)
        self.achievements.append(desc)
        return desc

    def battle(self, lvl):
        if not 1 <= lvl <= 100:
            return "Invalid level"
        diff = lvl - self.level
        if diff < -1:
            return "Easy fight"
        if diff < 1:
            self.__incr_exp(5 * (diff + 2))
            return "A good fight"
        if diff < 5 or self.level // 10 == lvl // 10:
            self.__incr_exp(20 * diff * diff)
            return "An intense fight"
        return "You've been defeated"
