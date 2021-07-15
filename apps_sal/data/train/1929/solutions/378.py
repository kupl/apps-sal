from collections import defaultdict
def tree():
    return defaultdict(tree)

class StreamChecker:
    def __init__(self, words: List[str]):
        # we store the words in an inverse trie (nexted dictionary) because when we get a new query we would know the last character to match and from that if we move upwards we will know whether we reach the top or not if we do we found our word else we return False  
        # to achieve this we need to construct an inverse trie and thus we won't have multiple choices to match we would only have a single choice for each character
        self.trie = defaultdict(tree)
        for word in words:
            node = self.trie
            for char in word[::-1]:
                node = node[char]
            node['*'] = 1
        self.current_list = []
        
#         self.print_nested(self.trie)
        
#     def print_nested(self, d, indent=0):
#         for k, v in d.items():
#             print ('{}{!r}:'.format(indent * '  ', k))
#             if type(v) is not int:
#                 self.print_nested(v, indent + 1)

    def query(self, letter: str) -> bool:
        # there are two reasons for returning false one is that we did not find a matching character in the tire for the current letter in which case we can empty the entire list
        # else if we found a matching a character but its not marking the end of the search(here beginning of the word) we add it to the list and return False
        # currently we will store the words in a simple list if we return false for them and if we return true we remove them from the list
        # we first travel down the trie
        match_found = True
        end_found = False
        self.current_list.insert(0,letter)
        i = 0
        node = self.trie
        while i < len(self.current_list):
            if self.current_list[i] in list(node.keys()):
                node = node[self.current_list[i]]
                if '*' in list(node.keys()):
                    end_found = True
                    break
            else:
                match_found = False
                break
            i += 1      
        if '*' in list(node.keys()):
            end_found = True
        # if (not match_found):
        #     self.current_list = [letter]
        return end_found
    
    # for the following approach only `6 out of 17 test cases pass and so when we are travelling the stack the time limit exceeds this is because with the stack approach we are searching the words from the begining to the end and we do not know how many characters to match 
    '''
    def __init__(self, words: List[str]):
        # we store the words in a trie (nested defaultdictionary)
        self.trie = defaultdict(tree)
        for word in words:
            node = self.trie
            for char in word:
                node = node[char]
            node['*'] = 1
        self.pointers_stack = []
        # we keep a list of pointers which mark the beginnign of the words in the trie based on the queries in the trie and if we return True we just increment the last pointer in the pointers heirarchy to point to the new root down the hierarchy and if there is a new word that starts 
        # if we return False because we cannot find the current character in the current pointer we change the pointer to point to the beginning and if there is a word starting from that character we change it to it else we keep it null
        # if we return False because we have not yet reached the end of the word however we have a corresponding character in the current pointer then we make a new entry to the pointers list which marks that this character may be because a new word has begun change the pointer to point to the latest character 
        
    # def print_nested(self, d, indent=0):
    #     for k, v in d.items():
    #         print ('{}{!r}:'.format(indent * '  ', k))
    #         self.print_nested(v, indent + 1)

    def query(self, letter: str) -> bool:
        # we keep on poping elements from the pointer stack as they mark the beginning of the words 
        # so our stack will be like [#q1q2q3, #q2q3, #q3] (actually it will be [#q3,#q3,#q3] and all q3 will be different nodes ) if we find the current character in q3 we increment the pointer in the last element and so now our stack becomes [#q1q2q3, #q2q3, #q3q4] -
        # we keep on travelling the stack and if we do not find q4 somewhere we pop that node else we add q4 by incrementing the pointer till for all the elements in the stack
        # eg there is no word starting with q2 and having q4 while there are some words having #q1q2q3q4 and #q3q4 format then our stack will look like [#q1q2q3q4, #q3q4] 
        # if for some value we find a word ending in q4 we return True else we return False
        answer = False
        if self.pointers_stack != []:
            index = 0
            while index < len(self.pointers_stack) and self.pointers_stack != []:
                root = self.pointers_stack[index]
                if letter in root.keys():
                    self.pointers_stack[index] = root[letter]
                    if root[letter]['*'] == 1:
                        answer = True
                    index += 1
                else:
                    self.pointers_stack.pop(index)
        # finally we also need to add the current letter as a start of the word
        if letter in self.trie.keys():
            root = self.trie[letter]
            self.pointers_stack.append(root)
            if root['*'] == 1:
                answer = True
        return answer
        
    '''
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

