_end = '_end_'


class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = {}
        self.nodes_for_letters = []
        for word in words:
            self.add_to_trie(word)

    def add_to_trie(self, word):
        current = self.trie
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[_end] = _end

    def query(self, letter: str) -> bool:
        potential_nodes = self.nodes_for_letters + [self.trie]
        self.nodes_for_letters = [node[letter] for node in potential_nodes if letter in node]
        return any((_end in node) for node in self.nodes_for_letters)
