class StreamChecker:

    def __init__(self, words: List[str]):
        self.waitlist = []
        self.trie = dict()
        for w in words:
            temp_dict = self.trie
            for letter in w:
                temp_dict = temp_dict.setdefault(letter, dict())
            temp_dict['#'] = '#'

    def query(self, letter: str) -> bool:
        waitlist = []
        if letter in self.trie:
            waitlist.append(self.trie[letter])
        for item in self.waitlist:
            if letter in item:
                waitlist.append(item[letter])
        self.waitlist = waitlist
        return any(('#' in item for item in self.waitlist))
