class StreamChecker:

    def __init__(self, words: List[str]):
        self.wait_list = []
        self.trie = dict()
        for w in words:
            temp_dict = self.trie
            for c in w:
                temp_dict = temp_dict.setdefault(c, dict())
            temp_dict['#'] = '#'

    def query(self, letter: str) -> bool:
        new_wait = []
        if letter in self.trie:
            new_wait.append(self.trie[letter])
        for item in self.wait_list:
            if letter in item:
                new_wait.append(item[letter])
        self.wait_list = new_wait
        return any(('#' in wait for wait in self.wait_list))
