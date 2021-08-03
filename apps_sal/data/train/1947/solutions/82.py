class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        counter = [0] * 26
        for word in B:
            tmp = [0] * 26
            for c in map(lambda x: ord(x) - ord('a'), word):
                tmp[c] += 1
            for c in range(26):
                counter[c] = max(counter[c], tmp[c])

        ans = []
        for word in A:
            tmp = [0] * 26
            for c in map(lambda x: ord(x) - ord('a'), word):
                tmp[c] += 1
            if all(counter[c] <= tmp[c] for c in range(26)):
                ans.append(word)

        return ans
