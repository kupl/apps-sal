class StreamChecker:

    def __init__(self, words):
        self.waitlist = []
        self.trie = dict()

        for word in words:
            tmp_dict = self.trie
            for c in word:
                # update our temporary dict and add our current letter and a sub-dictionary
                # if key is not in dict, setdefault() will add {key:{}} and return default value {}
                # otherwise it will directly return the existing value of key
                tmp_dict = tmp_dict.setdefault(c, dict())

            tmp_dict['#'] = '#'

    def query(self, letter: str) -> bool:
        waitlist = []

        if letter in self.trie:
            waitlist.append(self.trie[letter])

        for item in self.waitlist:
            if letter in item:
                waitlist.append(item[letter])

        self.waitlist = waitlist

        return any('#' in item for item in self.waitlist)
