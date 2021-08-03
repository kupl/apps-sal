class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.curr + 1]
        self.history += [url]
        self.curr += 1
        print((self.history, self.curr))

    def back(self, steps: int) -> str:
        if self.curr < steps:
            self.curr = 0

        else:
            self.curr -= steps
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        if self.curr + steps > len(self.history) - 1:
            self.curr = len(self.history) - 1
        else:
            self.curr += steps
        return self.history[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
