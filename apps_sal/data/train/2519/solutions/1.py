class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(' ')
        a = []
        for i in range(len(sentence)):
            if len(sentence[i]) >= len(searchWord):
                if sentence[i][0:len(searchWord)] == searchWord:
                    a.append(i)
        if a:
            return min(a)+1
        else:
            return -1
