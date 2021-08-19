class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_root = dict()
        self.original_words = None

    def buildDict(self, dictionary):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """

        def add_word(trie_root, word):
            p = trie_root
            for character in word:
                if character not in p:
                    p[character] = dict()
                p = p[character]
            p['\x00'] = True
        self.original_words = set(dictionary)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        "\n         active_tries = list()\n         active_tries.append(self.trie_root)\n         is_tolerable = True\n         \n         for character in word:\n             next_active_tries = list()\n             for trie in active_tries:\n                 if character in trie:\n                     next_active_tries.append(trie[character])\n                 if character not in trie:\n                     if is_tolerable:\n                         is_tolerable = False\n                         for c, next_trie in trie.items():\n                             if c != '\x00':\n                                 next_active_tries.append(next_trie)\n             active_tries = next_active_tries\n             if not active_tries:\n                 break\n         \n         return any('\x00' in trie for trie in active_tries) and not is_tolerable\n         "
        charset = 'abcdefghijklmnopqrstuvwxyz'
        for (index, character) in enumerate(word):
            for replaced_character in charset:
                if character != replaced_character:
                    if word[:index] + replaced_character + word[index + 1:] in self.original_words:
                        return True
        return False
