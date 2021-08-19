class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.l = dict

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        n = len(word)
        for wo in self.l:
            if len(wo) == n and wo != word:
                for i in range(n):
                    if wo[:i] + wo[i + 1:] == word[:i] + word[i + 1:]:
                        return True
        return False
