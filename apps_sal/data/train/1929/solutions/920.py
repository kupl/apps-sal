class StreamChecker:

    def __init__(self, words: List[str]):
        self.waitlist = []

        def T():
            return collections.defaultdict(T)
        self.trie = T()
        for word in words:
            temp_dict = self.trie
            for letter in word:
                temp_dict = temp_dict[letter]
            temp_dict['#'] = True

    def query(self, letter: str) -> bool:
        waitlist = []
        if letter in self.trie:
            waitlist.append(self.trie[letter])
        for item in self.waitlist:
            if letter in item:
                waitlist.append(item[letter])
        self.waitlist = waitlist
        return any(('#' in item for item in self.waitlist))
