class Warrior():
    
    def __init__(self):
        self.rankList = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        
        self.level = 1
        self.experience = 100
        self.rank = "Pushover"
        self.achievements = []
        pass
    
    def gainXP(self, xp):
        if self.experience + xp <= 10000:
            self.experience += xp
            self.level = int(self.experience / 100)
            self.rank = self.rankList[int(self.level/10)]
        else:
            self.experience = 10000
            self.level = 100
            self.rank = self.rankList[int(self.level/10)]
        
    def battle(self, enemyLevel):
        print(str(self.level) + " VS " + str(enemyLevel))
        if enemyLevel < 1 or enemyLevel > 100:
            return "Invalid level"
        
        if enemyLevel == self.level:
            self.gainXP(10)
            return "A good fight"
        elif enemyLevel == self.level - 1:
            self.gainXP(5)
            return "A good fight"
        elif int(enemyLevel/10) > int(self.level/10) and enemyLevel-4 > self.level:
            return "You've been defeated"
        elif enemyLevel > self.level:
            self.gainXP(20 * (enemyLevel - self.level) * (enemyLevel - self.level))
            return "An intense fight"
        else:
            return "Easy fight"
        
    def training(self, array):
        if self.level >= array[2]:
            self.gainXP(array[1])
            self.achievements.append(array[0])
            return array[0]
        else:
            return "Not strong enough"
