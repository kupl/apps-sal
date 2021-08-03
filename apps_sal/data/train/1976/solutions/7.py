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

            p['\0'] = True

        # for word in dictionary:
        #    add_word(self.trie_root, word)
        self.original_words = set(dictionary)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """

        """
         active_tries = list()
         active_tries.append(self.trie_root)
         is_tolerable = True
         
         for character in word:
             next_active_tries = list()
             for trie in active_tries:
                 if character in trie:
                     next_active_tries.append(trie[character])
                 if character not in trie:
                     if is_tolerable:
                         is_tolerable = False
                         for c, next_trie in trie.items():
                             if c != '\0':
                                 next_active_tries.append(next_trie)
             active_tries = next_active_tries
             if not active_tries:
                 break
         
         return any('\0' in trie for trie in active_tries) and not is_tolerable
         """

        charset = "abcdefghijklmnopqrstuvwxyz"

        for index, character in enumerate(word):
            for replaced_character in charset:
                if character != replaced_character:
                    if word[:index] + replaced_character + word[index + 1:] in self.original_words:
                        return True

        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
