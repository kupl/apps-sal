class Solution:
    def isAnagram(self, s, t):
        word = dict()
        for i in s:
            if i not in word:
                word[i] = 1
            else:
                word[i] += 1

        for i in t:
            if i not in word:
                return False
            else:
                word[i] -= 1

        for i in word:
            if word[i] != 0:
                return False
        return True
