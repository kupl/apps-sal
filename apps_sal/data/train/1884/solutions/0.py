class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordDict = set(wordList)
        if endWord not in wordDict:
            return []
        wordDict.discard(beginWord)
        front, back = set([beginWord]), set([endWord])
        length = 2
        direction = 1
        parents = collections.defaultdict(set)

        while front:
            next_level = set()
            for word in front:
                for index in range(len(beginWord)):
                    p1, p2 = word[:index], word[index + 1:]
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        if word[index] != ch:
                            next_word = p1 + ch + p2
                            if next_word in wordDict:
                                next_level.add(next_word)
                                if direction == 1:
                                    parents[next_word].add(word)
                                else:
                                    parents[word].add(next_word)

            if next_level & back:
                res = [[endWord]]
                while res and res[0][0] != beginWord:
                    res = [[p] + r for r in res for p in parents[r[0]]]
                return res

            length += 1
            front = next_level
            if len(front) > len(back):
                direction *= -1
                front, back = back, front
            wordDict -= front
        return []

        """
         :type beginWord: str
         :type endWord: str
         :type wordList: List[str]
         :rtype: List[List[str]]
         """
