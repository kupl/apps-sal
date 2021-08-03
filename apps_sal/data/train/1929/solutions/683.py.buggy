# Solution 3: Trie (Accepted)
# Only a part of suffixes can be the prefix of a word,
# waiting for characters coming to form a complete word.
# Instead of checking all W suffixes in each query,
# we can just save those possible waiting prefixes in a waiting list.

# Explanation
# Initialization:

# Construct a trie
# declare a nonlocal waiting list.
# Query:

# for each node in the waiting list,
# check if there is child node for the new character.
# If so, add it to the new waiting list.
# return true if any node in the waitinglist is the end of a word.
# Time Complexity:
# waiting.size <= W, where W is the maximum length of words.
# So that O(query) = O(waiting.size) = O(W)
# We will make Q queries, the overall time complexity is O(QW)

# Note that it has same complexity in the worst case as solution 2 (like \"aaaaaaaa\" for words and query),
# In general cases, it saves time checking all suffixes, and also the set search in a big set.

# Space Complexity:

# waiting.size <= W, where W is the maximum length of words.
# waiting list will take O(W)

# Assume we have initially N words, at most N leaves in the trie.
# The size of trie is O(NW).

# Python:
# Time: 6000+ms

class StreamChecker(object):

    def __init__(self, words):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in words: reduce(dict.__getitem__, w, self.trie)['#'] = True
        self.waiting = []

    def query(self, letter):
        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        return any(\"#\" in node for node in self.waiting)
    
    

#     class StreamChecker(object):

#     def __init__(self, words):
#         \"\"\"
#         :type words: List[str]
#         \"\"\"      
#         self.waitlist = []
#         self.trie = dict()
#         for word in words:
#             # create a temporary dict based off our root dict object
#             temp_dict = self.trie
#             for letter in word:
#                 # update our temporary dict and add our current letter and a sub-dictionary
#                 # if key is not in dict, setdefault() will add {key:{}} and return default value {}
#                 # otherwise it will directly return the existing value of key
#                 temp_dict = temp_dict.setdefault(letter, dict())
#             # If our word is finished, add {'#': '#'} at the stopping node
#             temp_dict['#'] = '#'

#     def query(self, letter):
#         \"\"\"
#         :type letter: str
#         :rtype: bool
#         \"\"\"
#         waitlist = []
#         # if letter can be the prefix of word
#         if letter in self.trie:
#             waitlist.append(self.trie[letter])
#         # for each possible prefix, append letter if the new substr still can be a prefix
#         for item in self.waitlist:
#             if letter in item:
#                 waitlist.append(item[letter])
                
#         self.waitlist = waitlist
#         return any('#' in item for item in self.waitlist)
