class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        record = {o: i for (i, o) in enumerate(order)}

        def checkOrdered(w1, w2):
            p = min(len(w1), len(w2))
            i = 0
            while i < p:
                if w1[i] == w2[i]:
                    i += 1
                else:
                    break
            if i != p:
                (l, r) = (record[w1[i]], record[w2[i]])
                if l < r:
                    return True
                if l > r:
                    return False
            else:
                return len(w1) <= len(w2)
        if len(words) <= 1:
            return True
        left = self.isAlienSorted(words[:len(words) // 2], order)
        mid = checkOrdered(words[len(words) // 2 - 1], words[len(words) // 2])
        right = self.isAlienSorted(words[len(words) // 2:], order)
        return left and right and mid
