class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        self.END = '0'
        self.q = ''
        for word in words:
            curr_dict = self.root
            for letter in word[::-1]:
                curr_dict = curr_dict.setdefault(letter, {})
            curr_dict[self.END] = self.END

    def query(self, letter: str) -> bool:
        self.q += letter
        curr_node = self.root
        for l in self.q[::-1]:
            if l in curr_node:
                curr_node = curr_node.get(l)
            else:
                return False
            if self.END in curr_node:
                return True
        return False
