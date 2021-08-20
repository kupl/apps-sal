class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hsh = collections.defaultdict(list)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.hsh[len(word)].append(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return any((sum((x != y for (x, y) in zip(word, candidate))) == 1 for candidate in self.hsh[len(word)]))
