_end = '_end'

def make_trie(words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return root

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = make_trie(words)
        self.cur_tries = []

    def query(self, letter: str) -> bool:
        new_tries = []
        result = False
        for tr in self.cur_tries + [self.trie]:
            if letter in tr:
                if _end in tr[letter]:
                    result = True
                if _end not in tr[letter] or len(tr[letter]) > 1:
                    new_tries.append(tr[letter])
        self.cur_tries = new_tries   
        
        return result
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

