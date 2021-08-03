class StreamChecker:

    def __init__(self, words: List[str]):

        self.queries = []
        trie = {}
        for word in words:
            word = list(reversed(word))
            here = trie
            for i in range(len(word)):
                if word[i] not in list(here.keys()):
                    here[word[i]] = {}
                here = here[word[i]]
            here['is_word'] = True

        self.trie = trie

    def query(self, letter: str) -> bool:
        self.queries.append(letter)

        here = self.trie
        for i in range(1, len(self.queries) + 1):
            if self.queries[-i] not in list(here.keys()):
                return False
            here = here[self.queries[-i]]
            if 'is_word' in list(here.keys()):
                return True

        # for i in range(1, min(len(self.queries), self.max_len) + 1):
        #     if i in self.vocab.keys():
        #         word = \"\".join(self.queries[-i:])
        #         if word in self.vocab[i]:
        #             return True
        # return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
