class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = homepage
        self.backw = []
        self.forw = []
        

    def visit(self, url: str) -> None:
        self.backw.append(self.curr)
        self.forw = []
        self.curr = url

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.backw: break
            self.forw.append(self.curr)
            self.curr = self.backw.pop()
        return self.curr
        
    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.forw: break
            self.backw.append(self.curr)
            self.curr = self.forw.pop()
        return self.curr


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

