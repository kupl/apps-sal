class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = 0
        self.history = [homepage]
        self.bound = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr == len(self.history):
            self.history.append(url)
            self.bound += 1
        else:
            self.history[self.curr] = url
            self.bound = self.curr

    def back(self, steps: int) -> str:
        move = max(self.curr - steps, 0)
        self.curr = move
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        move = min(self.bound, self.curr + steps)
        self.curr = move
        return self.history[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
