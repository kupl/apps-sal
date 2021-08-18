class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_set = {}
        self.word_origin = set([])

    def candidate(self, word):
        result = []
        for i in range(len(word)):
            result.append(word[0:i] + '*' + word[i + 1:])
        return result

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.word_set = {}
        self.word_origin = set(dict)
        for item in dict:
            for cand in self.candidate(item):
                self.word_set[cand] = self.word_set.get(cand, 0) + 1

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for cand in self.candidate(word):
            if (self.word_set.get(cand, 0) > 1 or (self.word_set.get(cand, 0) == 1 and word not in self.word_origin)):
                return True
        return False
