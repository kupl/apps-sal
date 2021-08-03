class BrowserHistory:

    def __init__(self, homepage: str):
        self.fwd = []
        self.bck = [homepage]

    def visit(self, url: str) -> None:
        self.bck.append(url)
        self.fwd = []

    def back(self, steps: int) -> str:
        el = None
        while steps and len(self.bck) > 1:
            self.fwd.append(self.bck.pop())
            steps -= 1
        return self.bck[-1]

    def forward(self, steps: int) -> str:
        el = None
        while steps and self.fwd:
            self.bck.append(self.fwd.pop())
            steps -= 1
        return self.bck[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
