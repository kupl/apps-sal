class StreamChecker:

    def __init__(self, words: List[str]):
        self.waitlist = []
        self.trie = dict()
        for word in words:
            temp_dict = self.trie
            for letter in word:
                temp_dict = temp_dict.setdefault(letter, dict())
            temp_dict['#'] = '#'

    def query(self, letter):
        \"\"\"
        :type letter: str
        :rtype: bool
        \"\"\"
        waitlist = []
        if letter in self.trie:
            waitlist.append(self.trie[letter])
        for item in self.waitlist:
            if letter in item:
                waitlist.append(item[letter])
                
        self.waitlist = waitlist
        return any('#' in item for item in self.waitlist)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
