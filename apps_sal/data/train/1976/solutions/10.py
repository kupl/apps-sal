class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.magic_dict = set()

    def buildDict(self, words):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in words:
            for i in range(len(word)):
                for char in range(26):
                    char = chr(ord('a') + char)
                    if char != word[i]:
                        self.magic_dict.add(word[:i] + char + word[i + 1:])

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return word in self.magic_dict


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
