# class StreamChecker:

#     def __init__(self, words: List[str]):
#         # self.words=words
#         self.last=defaultdict(list)
#         for _ in words:
#             self.last[_[-1]].append(_)
#         self.read=[]

#     def query(self, letter: str) -> bool:
#         self.read.append(letter)
#         ret=False
#         poss=self.last.get(letter)
#         if poss:
#             for _ in poss:
#                 ind=len(self.read)-1
#                 suc=True
#                 for i in range(len(_)-1,-1,-1):
#                     if ind == -1:break
#                     if self.read[ind]!=_[i]:
#                         suc=False
#                         break
#                     ind-=1
#                 if suc:
#                     ret=suc
#                     break
#         return ret
                

# # Your StreamChecker object will be instantiated and called as such:
# # obj = StreamChecker(words)
# # param_1 = obj.query(letter)
class StreamChecker:

    def __init__(self, words: List[str]):
        self.history = \"\"
        self.map = {}
        
        for word in words:
            curr_node = self.map
            for letter in word[::-1]:
                if letter not in curr_node:
                    curr_node[letter] = {}
                curr_node = curr_node[letter]
            curr_node['#'] = {}

    def query(self, letter: str) -> bool:
        self.history += letter

        curr_node = self.map
        for l in self.history[::-1]:

            if l not in curr_node:
                return False
                    
            curr_node = curr_node[l]
        
            if '#' in curr_node:
                return True
        
        return False
