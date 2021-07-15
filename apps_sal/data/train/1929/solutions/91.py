class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        
        for word in words:
            curnode = self.root
            for ch in word:
                if ch not in curnode:
                    curnode[ch] = {}
                curnode = curnode[ch]
            curnode['is_end'] = True
        
        self.leads = [self.root] # the pointers to the threads we follow right now

    def query(self, letter: str) -> bool:
        next_leads = [self.root]
        found_word = False
        
        for lead in self.leads:
            if letter in lead:
                new_lead = lead[letter]
                next_leads.append(new_lead)
                if 'is_end' in new_lead:
                    found_word = True
            
        self.leads = next_leads
        return found_word
    
    
    
# class TrieNode:
#     def __init__(self, is_end=False):
#         self.children = {}  # char to trie node
#         self.is_end = is_end

# class StreamChecker:

#     def __init__(self, words: List[str]):
#         self.root = TrieNode()
        
#         for word in words:
#             curnode = self.root
#             for ch in word:
#                 if ch not in curnode.children:
#                     curnode.children[ch] = TrieNode()
#                 curnode = curnode.children[ch]
            
#             curnode.is_end = True
        
#         self.leads = set([self.root]) # the pointers to the threads we follow right now

#     def query(self, letter: str) -> bool:
#         next_leads = set([self.root])
#         found_word = False
        
#         for lead in self.leads:
#             if letter in lead.children:
#                 next_leads.add(lead.children[letter])
#                 if lead.children[letter].is_end:
#                     found_word = True
            
#         self.leads = next_leads
#         return found_word

