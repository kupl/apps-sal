class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_set = collections.Counter(chars)
        N = len(chars)
        result = 0
        for i in words:
            if len(i) <= N and self.check(char_set, i):
                result += len(i)
        return result

    def check(self, char_ctr, S):
        S_ctr = collections.Counter(S)
        for i in S_ctr:
            if i not in char_ctr or S_ctr[i] > char_ctr[i]:
                return False
        return True
