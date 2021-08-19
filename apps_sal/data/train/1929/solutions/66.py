class TRIE:

    def __init__(self, next_letters=None, flag=False):
        if not next_letters:
            self.next_letters = {}
        else:
            self.next_letters = next_letters
        self.flag = flag


class StreamChecker:

    def __init__(self, words: List[str]):
        # build a trie
        self.root = TRIE()
        for word in words:
            curr_node = self.root
            for l in word:
                if l not in curr_node.next_letters:
                    new_node = TRIE()
                    curr_node.next_letters[l] = new_node
                    curr_node = new_node
                else:
                    curr_node = curr_node.next_letters[l]
            curr_node.flag = True
        # a collection of curr_nodes
        self.curr_nodes = set([self.root])

    def query(self, letter: str) -> bool:
        found = False
        new_curr_nodes = set([self.root])  # always add back root
        for node in self.curr_nodes:
            if letter in node.next_letters:
                curr_node = node.next_letters[letter]
                new_curr_nodes.add(curr_node)
                if curr_node.flag:
                    found = True
        self.curr_nodes = new_curr_nodes
        return found


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
