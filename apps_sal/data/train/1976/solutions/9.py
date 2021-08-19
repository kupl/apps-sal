class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = set()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.dict.add(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        letters = string.ascii_lowercase
        for i in range(len(word)):
            for letter in letters:
                if letter != word[i]:
                    if word[:i] + letter + word[i + 1:] in self.dict:
                        return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
