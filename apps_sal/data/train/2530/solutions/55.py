class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        total = 0
        complements = defaultdict(int)
        
        for song in time:
            modRem = song % 60
            tempTotal = 60 - modRem
            if tempTotal in complements:
                total += complements[tempTotal]
            complements[modRem] += 1
            if (modRem == 0): complements[60] += 1
        return total
