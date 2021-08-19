class Warrior:

    def __init__(self):
        self.level = 1
        self.maxLevel = 100
        self.experience = 100
        self.ranks = ['Pushover', 'Novice', 'Fighter', 'Warrior', 'Veteran', 'Sage', 'Elite', 'Conqueror', 'Champion', 'Master', 'Greatest']
        self.rank = 'Pushover'
        self.achievements = []

    def calculateRank(self, enemyLevel=None):
        if not enemyLevel:
            try:
                self.rank = self.ranks[int(self.level / 10)]
                return self.rank
            except Exception as e:
                self.rank = 'Greatest'
                return 'Greatest'
        else:
            return self.ranks[int(enemyLevel / 10)]

    def calculateLevel(self):
        self.level = int(self.experience / 100)
        self.calculateRank()

    def increaseExperience(self, amount):
        if self.experience + amount > 10000:
            self.experience = 10000
        else:
            self.experience += amount
        self.calculateLevel()

    def battle(self, enemyLevel):
        if enemyLevel > 100 or enemyLevel < 1:
            return 'Invalid level'
        levelDiff = self.level - enemyLevel
        if enemyLevel == self.level:
            self.increaseExperience(10)
            return 'A good fight'
        if levelDiff == 1:
            self.increaseExperience(5)
            return 'A good fight'
        if levelDiff >= 2:
            return 'Easy fight'
        if levelDiff < 0:
            enemyRankIndex = self.ranks.index(self.calculateRank(enemyLevel=enemyLevel))
            warriorRankIndex = self.ranks.index(self.calculateRank())
            higherLevel = levelDiff * -1
            if enemyRankIndex - warriorRankIndex >= 1 and higherLevel >= 5:
                return "You've been defeated"
            experienceGained = 20 * higherLevel * higherLevel
            self.increaseExperience(experienceGained)
            return 'An intense fight'

    def training(self, args):
        note = args[0]
        experienceEarned = args[1]
        minLevel = args[2]
        if self.level >= minLevel:
            self.increaseExperience(experienceEarned)
            self.achievements.append(note)
            return note
        else:
            return 'Not strong enough'
