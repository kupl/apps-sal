class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict1 = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for i in dict:
            self.dict1[len(i)] = self.dict1.get(len(i), []) + [i]

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in self.dict1.get(len(word), []):
            count = 0
            for j in range(len(word)):
                if i[j] != word[j]:
                    count += 1
            if count == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
