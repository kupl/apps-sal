class BrowserHistory:

    def __init__(self, homepage: str):
        # self.list = []
        # self.list.append(homepage)
        # self.currentIndex = 0
        self.forwardA = []
        self.backward = [homepage]
        

    def visit(self, url: str) -> None:
        self.backward.append(url)
        self.forwardA = []
        
#         self.currentIndex += 1
#         while self.currentIndex < len(self.list):
#             self.list.pop()
            
#         self.list.append(url)
        
    #Move forward n steps
    def forward(self, steps: int) -> str:
        # self.currentIndex = min(self.currentIndex+steps,len(self.list)-1)
        # return self.list[self.currentIndex]
        i = 0
        while len(self.forwardA) != 0 and i < steps:
            i += 1
            item = self.forwardA.pop()
            self.backward.append(item)
        return self.backward[-1]
        
        
        
    def back(self, steps: int) -> str:
        # self.currentIndex = max(self.currentIndex-steps,0)
        # return self.list[self.currentIndex]
        i = 0
        while len(self.backward) > 1 and i < steps:
            item = self.backward.pop()
            self.forwardA.append(item)
            i += 1
        return self.backward[-1]
        
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

