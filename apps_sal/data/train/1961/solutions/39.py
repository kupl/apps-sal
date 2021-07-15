class BrowserHistory:

    def __init__(self, homepage: str):
        self.curIndex = 0
        self.history = [homepage]
        
    def visit(self, url: str) -> None:
        self.history = self.history[:self.curIndex + 1]
        self.history.append(url)
        self.curIndex += 1

    def back(self, steps: int) -> str:
        self.curIndex = max(0, self.curIndex - steps)
        return self.history[self.curIndex]

    def forward(self, steps: int) -> str:
        self.curIndex = min(len(self.history) - 1, self.curIndex + steps)
        return self.history[self.curIndex]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

