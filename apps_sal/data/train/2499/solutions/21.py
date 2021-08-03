class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = collections.Counter(deck)
        parts = {}
        #for num in deck: d[num] = d.get(num,0)+1
        for key in d:
            m = d[key]
            if(m == 1):
                return False
            parts[m] = parts.get(m, 0) + 1
            i = 2
            while(m / i >= 2):
                if(m % i == 0):
                    parts[m // i] = parts.get(m // i, 0) + 1
                i += 1
        for key in parts:
            if(parts[key] == len(d)):
                return True
        return False
