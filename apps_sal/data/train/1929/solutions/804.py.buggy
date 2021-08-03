class StreamChecker(object):

    def __init__(self, words):
        \"\"\"
        :type words: List[str]
        \"\"\"      
        self.waitlist = []
        self.trie = dict()
        for word in words:  
            temp_dict = self.trie
            for letter in word:
                # update our temporary dict and add our current letter and a sub-dictionary
                # if key is not in dict, setdefault() will add {key:{}} and return default value {}
                # otherwise it will directly return the existing value of key
                temp_dict = temp_dict.setdefault(letter, dict())
            temp_dict['#'] = '#'

    def query(self, letter):
        \"\"\"
        :type letter: str
        :rtype: bool
        \"\"\"
        waitlist = []
        # if letter can be the prefix of word
        if letter in self.trie:
            waitlist.append(self.trie[letter])
        # for each possible prefix, append letter if the new substr still can be a prefix
        for item in self.waitlist:
            if letter in item:
                waitlist.append(item[letter])
                
        self.waitlist = waitlist
        return any('#' in item for item in self.waitlist)
