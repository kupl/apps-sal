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
