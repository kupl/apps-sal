class StreamChecker(object):

    def __init__(self, words):
        \"\"\"
        :type words: List[str]
        \"\"\"      
        self.waitlist = []
        self.trie = dict()
        for word in words:
            # create a temporary dict based off our root dict object
            temp_dict = self.trie
            for letter in word:
                # update our temporary dict and add our current letter and a sub-dictionary
                # if key is not in dict, setdefault() will add {key:{}} and return default value {}
                # otherwise it will directly return the existing value of key
                temp_dict = temp_dict.setdefault(letter, dict())
            # If our word is finished, add {'#': '#'} at the stopping node
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
    

    # TLE
# class StreamChecker:

#     def __init__(self, words: List[str]):
#         self.wordDict = set(words)
#         self.streamDict = set()

#     def query(self, letter: str) -> bool:
#         existingKeys = list(self.streamDict)
#         newStreamDict = set()
#         found = False
#         for key in existingKeys+['']:
#             newStreamDict.add(key+letter)
#             if key+letter in self.wordDict:
#                 found = True
#         # print(newStreamDict)
#         self.streamDict = newStreamDict
#         return found


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
