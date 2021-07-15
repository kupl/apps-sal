class Warrior:
    def __init__(self):
        self.xp = 100
        self.ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        self.achievements = []

    @property
    def experience(self):
        return min(self.xp, 10000)
    @property
    def level(self):
        return self.experience//100
    @property
    def rank(self):
        return self.ranks[self.level//10]
    
    def battle(self, level):
        diff = level - self.level
        if not (0<level<=100): return "Invalid level"
        elif diff>4 and self.ranks.index(self.ranks[level//10]) > self.ranks.index(self.rank): return "You've been defeated"
        elif diff>0:
            self.xp += 20*diff*diff
            return "An intense fight"
        elif not diff:
            self.xp += 10
            return 'A good fight'
        elif diff==-1:
            self.xp += 5
            return 'A good fight'
        return "Easy fight"

    def training(self, arr):
        if self.level >= arr[2]:
            self.xp += arr[1]
            self.achievements.append(arr[0])
            return arr[0]
        return "Not strong enough"
