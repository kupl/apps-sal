class Node:
    def __init__(self, val=None, children={}, is_end=False):
        self.val = val
        self.children = children
        self.is_end = is_end


class StreamChecker:
    def __add_word(self, word):
        curr = self.root
        # print(\"word\", word)
        for char in word[::-1]:
            # print(\"char\", char)
            if char not in curr.children:
                curr.children[char] = Node(val=char, children={}, is_end=False)
            curr = curr.children[char]
        curr.is_end = True

    def __init__(self, words: List[str]):
        self.root = Node(None, {}, False)
        self.buffer = []
        for word in words:
            self.__add_word(word)

    def __is_present_k(self):
        curr = self.root
        # print(\"buffer\", self.buffer)
        for char in self.buffer:
            # print(\"char\", char)
            # print(\"curr children\", [ curr.children[temp].val for temp in curr.children] )
            if char not in curr.children:
                return False
            curr = curr.children[char]
            if curr.is_end:
                return True
        return False

    def query(self, letter: str) -> bool:
        self.buffer.insert(0, letter)
        return self.__is_present_k()

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
