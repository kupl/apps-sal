class Warrior():
    def __init__(self):
        self.level = 1
        self.experience = 100
        self.rank = "Pushover"
        self.achievements = []
        self.max_level = 100
        self.available_ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]

    def battle(self, enemy_level):
        if enemy_level < 1 or enemy_level > 100:
            return "Invalid level"
        if enemy_level <= self.level:
            diff = self.level - enemy_level
            self._get_experience(10 // (diff + 1))
            if diff > 1:
                return "Easy fight"
            else:
                return "A good fight"
        else:
            diff = enemy_level - self.level
            if diff >= 5 and enemy_level // 10 > self.level // 10:
                return "You've been defeated"
            else:
                self._get_experience(20 * diff * diff)
                return "An intense fight"

    def training(self, achievement):
        description = achievement[0]
        experience = achievement[1]
        min_level = achievement[2]
        if self.level >= min_level:
            self.achievements.append(description)
            self._get_experience(experience)
            return description
        else:
            return "Not strong enough"

    def _get_experience(self, experience):
        if experience >= 5:
            self.experience += experience
            self.level = self.experience // 100
            if self.level >= self.max_level:
                self.level = self.max_level
                self.experience = self.max_level * 100
            self.rank = self.available_ranks[self.experience // 1000]
