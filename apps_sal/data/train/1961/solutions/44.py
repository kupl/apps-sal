class BrowserHistory:

    def __init__(self, homepage: str):
        \"\"\"
        :type homepage: str
        \"\"\"
        self.history = [homepage]
        self.index = 0
        

    def visit(self, url):
        \"\"\"
        :type url: str
        :rtype: None
        \"\"\"
        self.history = self.history[:self.index + 1]
        self.history.append(url)
        self.index = len(self.history) - 1
        

    def back(self, steps):
        \"\"\"
        :type steps: int
        :rtype: str
        \"\"\"
        self.index = max(0, self.index - steps)
        return self.history[self.index]
        

    def forward(self, steps):
        \"\"\"
        :type steps: int
        :rtype: str
        \"\"\"
        self.index = min(len(self.history) - 1, self.index + steps)
        return self.history[self.index]    

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
