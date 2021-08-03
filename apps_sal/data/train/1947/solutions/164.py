class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        um = {}
        result = []
        for b in B:
            for letter in b:
                if letter not in um:
                    um[letter] = b.count(letter)
                elif b.count(letter) > um[letter]:
                    um[letter] = b.count(letter)
        for a in A:
            boola = True
            for i, n in um.items():
                if (i not in a) or a.count(i) < n:
                    boola = False
                    break
            if boola:
                result.append(a)
        return result
