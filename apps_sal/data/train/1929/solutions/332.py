class Trie:
    def __init__(self, letter):
        self.next_letters = dict()
        self.letter = letter
        self.is_end_word = False

    def add_word(self, word, idx):
        if idx == -1:
            self.is_end_word = True
            return
        if word[idx] not in self.next_letters:
            self.next_letters[word[idx]] = Trie(word[idx])
        self.next_letters[word[idx]].add_word(word, idx - 1)


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie('')
        for w in words:
            self.trie.add_word(w, len(w) - 1)
        self.history = list()

    def query(self, letter: str) -> bool:
        self.history.append(letter)
        cur_node = self.trie
        idx = len(self.history) - 1
        while idx >= 0 and self.history[idx] in cur_node.next_letters:
            c = self.history[idx]
            cur_node = cur_node.next_letters[c]
            if cur_node.is_end_word:
                return True
            idx -= 1
        return False
