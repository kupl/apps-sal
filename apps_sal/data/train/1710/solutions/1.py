class Warrior(object):
    MAX_LVL = 100
    MAX_XPS = 10000
    LVL_XP_RATIO = 100
    RANKS = ['', 'Pushover', 'Novice', 'Fighter', 'Warrior', 'Veteran', 'Sage', 'Elite', 'Conqueror', 'Champion', 'Master', 'Greatest']
    DEF_RET_ACHIEV = 'Not strong enough'
    INVALID_BATTLE = 'Invalid level'
    FAILED_BATTLE = "You've been defeated"
    STR_BATTLE = ['A good fight', 'An intense fight', 'Easy fight']

    def __init__(self):
        (self.xps, self.achiev) = (self.LVL_XP_RATIO, [])

    @property
    def level(self):
        return self.xps // self.LVL_XP_RATIO

    @property
    def rank(self):
        return self.RANKS[self.getRank(self.xps)]

    @property
    def experience(self):
        return self.xps

    @property
    def achievements(self):
        return self.achiev[:]

    def getRank(self, xps):
        return xps // 1000 + 1

    def updateXps(self, xp):
        self.xps = min(self.xps + xp, self.MAX_XPS)

    def battle(self, oLvl):
        diff = oLvl - self.level
        if not 1 <= oLvl <= self.MAX_LVL:
            return self.INVALID_BATTLE
        if diff >= 5 and self.getRank(self.xps) < self.getRank(oLvl * self.LVL_XP_RATIO):
            return self.FAILED_BATTLE
        xpGain = 20 * diff ** 2 if diff > 0 else max(0, 10 + 5 * diff)
        iRet = (diff > 0) - (diff < 0) if diff != -1 else 0
        self.updateXps(xpGain)
        return self.STR_BATTLE[iRet]

    def training(self, event):
        (ach, xpGain, minLvl) = event
        if self.level < minLvl:
            return self.DEF_RET_ACHIEV
        self.updateXps(xpGain)
        self.achiev.append(ach)
        return ach
