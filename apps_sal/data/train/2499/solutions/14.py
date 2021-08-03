class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck1 = list(set(deck))
        len1 = []
        for j in range(len(deck1)):
            leny = len([number for number in deck if number == deck1[j]])
            len1.append(leny)
        count = 2
        while(count <= len(deck)):
            if len(deck) % count == 0:
                ty = len([number for number in len1 if number % count > 0])
                if ty == 0:
                    return True
                    break
            count = count + 1
        return False
