class Warrior():
    rank_list = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage",
                 "Elite", "Conqueror", "Champion", "Master", "Greatest"]

    def __init__(self):
        self.level = 1
        self.experience = 100
        self.achievements = []

    @property
    def rank(self):
        return self.rank_list[self.level // 10]

    def get_experience(self, point):
        exp = self.experience + point
        self.experience = (exp, 10000)[exp >= 10000]
        self.level = self.experience // 100

    def training(self, lst):
        if lst[-1] <= self.level:
            achiev = lst[0]
            self.achievements.append(achiev)
            self.get_experience(lst[1])
            return achiev
        return "Not strong enough"

    def battle(self, enemy_level):
        if 0 < enemy_level < 101:
            return self.get_result(enemy_level)
        return "Invalid level"

    def get_result(self, enemy_level):
        diff = enemy_level - self.level
        if diff >= 5 and ((enemy_level // 10) - (self.level // 10)) > 0:
            return "You've been defeated"
        fight_result = {(1, 0, 1): "Easy fight", (1, 1, 0): "A good fight"}
        point = {-2: 0, -1: 5, 0: 10}.get((diff, -2)[diff < -1], 20 * (diff * diff))
        self.get_experience(point)
        return fight_result.get((point <= 10, point > 0, point == 0), "An intense fight")
