class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        self.history = self.history[0:self.i + 1]
        self.history.append(url)
        self.i += 1

    def back(self, steps: int) -> str:
        if self.i >= steps:
            for _ in range(steps):
                self.i -= 1
            return self.history[self.i]
        else:
            self.i = 0
            return self.history[self.i]

    def forward(self, steps: int) -> str:
        if len(self.history) - self.i - 1 >= steps:
            for _ in range(steps):
                self.i += 1
            return self.history[self.i]
        else:
            self.i = len(self.history) - 1
            return self.history[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
