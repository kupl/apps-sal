class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hashMap = {}
        boolean = False
        lenght = len(deck)
        if lenght < 2:
            return False

        def commonFactor(a, b):
            if(b == 0):
                return a
            else:
                return commonFactor(b, a % b)

        for i in range(lenght):
            if hashMap.get(deck[i]) is not None:
                hashMap[deck[i]] = hashMap[deck[i]] + 1
            else:
                hashMap[deck[i]] = 1

        for i in range(lenght):
            if hashMap[deck[i]] == 1:
                return False
            elif i < lenght - 1 and commonFactor(hashMap[deck[i]], hashMap[deck[i + 1]]) > 1:
                boolean = True
            elif i == lenght - 1 and commonFactor(hashMap[deck[i]], hashMap[deck[i - 1]]) > 1:
                boolean = True
            else:
                return False
        return boolean
