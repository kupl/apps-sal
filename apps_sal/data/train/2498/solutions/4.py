class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            s1,s2 = words[i],words[i+1]
            if not self.checkWords(s1,s2,order):
                return False
        return True
    
    def checkWords(self,s1,s2,order):
        for i in range(len(s1)):
            if i < len(s2):
                if s1[i] != s2[i]:
                    if order.index(s1[i]) > order.index(s2[i]): return False
                    return True
            else:
                return False
        return True
