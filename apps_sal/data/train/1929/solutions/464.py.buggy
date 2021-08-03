import string
class Node :
    def __init__(self):
        self.characters={}
        self.isEnd=False
class Trie :
    def __init__(self):
        self.root=None
    def insert(self,word):
        if self.root==None :
            self.root=Node()
        curr_node=self.root
        #print(curr_node.isEnd)
        n=len(word)
        i=0
        while i < n :
            #print(i)
            if word[i] not in curr_node.characters :
                node=Node()
                curr_node.characters[word[i]]=node
            curr_node=curr_node.characters[word[i]]
            if i==n-1 :
                curr_node.isEnd=True
            i+=1
            
    def print_words(self) :
        node=self.root
        q=[(node,\"\")]
        while len(q) > 0 :
            node,word=q.pop(0)
            if node.isEnd==True :
                print(word)
            for ch in node.characters :
                q.append((node.characters[ch],word+ch))
    def search(self, word: str) -> bool:
        \"\"\"
        Returns if the word is in the trie.
        \"\"\"
        if self.root==None :
            return False
        current_node=self.root
        current_index=0
        n=len(word)
        while current_index < n :
            if word[current_index] not in current_node.characters :
                return False
            current_node=current_node.characters[word[current_index]]
            current_index+=1
            if current_node.isEnd==True :
                return True
        return False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie=Trie()
        for word in words :
            #print(word[::-1])
            self.trie.insert(word[::-1])
        self.curr_string=\"\"
        #self.trie.print_words()

    def query(self, letter: str) -> bool:
        self.curr_string+=letter
        #print(self.curr_string[::-1])
        return self.trie.search(self.curr_string[::-1])
        # n=len(self.curr_string)
        # for i in range(n-1,-1,-1) :
        #     if self.trie.search(self.curr_string[i:n]) ==True :
        #         return True
        # return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
