class Trie:

    def __init__(self, words):
        self.trie = {}
        for word in words:
            self.add(word)

    def add(self, word):

        def add_helper(prev, i):
            if i == len(word) - 1:
                prev[word[i]] = {None: None}
                return
            char = word[i]
            if char not in prev:
                prev[char] = {}
            add_helper(prev[char], i + 1)
        add_helper(self.trie, 0)

    def contains(self, word):

        def dfs(prev, i):
            if i == len(word):
                return False
            if word[i] in prev and None in prev[word[i]]:
                return True
            return dfs(prev[word[i]], i + 1) if word[i] in prev else False
        return dfs(self.trie, 0)


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie([''.join(reversed(w)) for w in words])
        self.word = ''

    def query(self, letter: str) -> bool:
        self.word = ''.join([letter, self.word])
        return self.trie.contains(self.word)
