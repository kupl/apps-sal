import collections
class StreamChecker:

    def __init__(self, words: List[str]):
        self.waitlist=[]
        self.trie={}
        
        
        for word in words:
            t=self.trie
            for letter in word:
                \"\"\"if letter not in t:
                    t[letter]={}
                t=t[letter]\"\"\"
                t = t.setdefault(letter, {})
            t['#']='#'    
        #print('t',t)        
        #for word in words:
            #self.insert(word)
    def query(self, letter):

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



    # Your StreamChecker object will be instantiated and called as such:
    # obj = StreamChecker(words)
    # param_1 = obj.query(letter)
