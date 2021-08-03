class StreamChecker:
    STOP_CHAR = \"\
\"
    
    def __init__(self, words: List[str]):
        self.root = dict()
        self.pointers = list()
        for word in words:
            self.add(word)

    def add(self, word):
        word += self.STOP_CHAR
        root = self.root
        for char in word:
            if char not in root:
                root[char] = dict()
            
            root = root[char]
    
    def query(self, letter: str) -> bool:
        self.pointers = [
            pointer[letter]
            for pointer in self.pointers
            if pointer.get(letter) is not None
        ]
        new_pointer = self.root.get(letter)
        if new_pointer is not None:
            self.pointers.append(new_pointer)
        for pointer in self.pointers:
            if self.STOP_CHAR in pointer:
                return True
        return False
    
    
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
