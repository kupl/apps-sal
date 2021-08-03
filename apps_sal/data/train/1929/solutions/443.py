class StreamChecker:

    class Trie_node:
        def __init__(self, value):
            self.value = value
            self.children = {}

        def add_child(self, node, letter):
            self.children[letter] = node

        def is_child(self, letter):
            if letter in self.children:
                return True
            return False

        def get_child(self, letter):
            return self.children[letter]

    def __init__(self, words: List[str]):
        self.trie = self.Trie_node(-1)
        self.max_length = 0
        self.letter_list = []
        for word in words:
            current_node = self.trie
            self.max_length = self.max_length if len(word) < self.max_length else len(word)

            for index, letter in enumerate(word[::-1]):
                if(current_node.is_child(letter)):
                    if(index == len(word) - 1):
                        current_node.get_child(letter).value = 0
                else:
                    if(index == len(word) - 1):
                        current_node.add_child(self.Trie_node(0), letter)
                    else:
                        current_node.add_child(self.Trie_node(-1), letter)
                current_node = current_node.get_child(letter)
        print((self.trie.children))

    def query(self, letter: str) -> bool:
        self.letter_list.append(letter)
        if(len(self.letter_list) > self.max_length):
            self.letter_list.pop(0)
        top_node = self.trie
        for letter in self.letter_list[::-1]:
            if(top_node.is_child(letter)):
                top_node = top_node.get_child(letter)
                if(top_node.value == 0):
                    return True
            else:
                return False
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
