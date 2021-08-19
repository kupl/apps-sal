class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            self.add_word_to_trie(self.trie, word, 0)
        self.pointers = {}
        self.q_no = 0

    def query(self, letter: str) -> bool:
        self.q_no += 1
        self.pointers[self.q_no] = self.trie
        result = False
        to_delete = []
        for q_no, pointer in list(self.pointers.items()):
            if letter not in pointer:
                to_delete.append(q_no)
                continue
            self.pointers[q_no] = pointer[letter]
            result = result or 1 in self.pointers[q_no]
        for del_c in to_delete:
            del self.pointers[del_c]
        return result

    def add_word_to_trie(self, node, word, i):
        if i == len(word):
            node[1] = True
            return
        if word[i] not in node:
            node[word[i]] = {}
        self.add_word_to_trie(node[word[i]], word, i + 1)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
