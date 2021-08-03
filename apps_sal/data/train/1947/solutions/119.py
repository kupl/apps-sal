class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        superword = [0] * 26
        result = []
        for word in B:
            current = [0] * 26
            for ch in word:
                i = ord(ch) - ord('a')
                current[i] += 1

            for i in range(26):
                superword[i] = max(superword[i], current[i])

        for word in A:
            current = [0] * 26
            for ch in word:
                i = ord(ch) - ord('a')
                current[i] += 1

            found = True
            for i in range(26):
                if superword[i] > current[i]:
                    found = False
                    break

            if found == True:
                result.append(word)

        return result
