class BrowserHistory:

    def __init__(self, homepage: str):
        self.prev = [homepage]
        self.future = []

    def visit(self, url: str) -> None:
        self.prev.append(url)
        self.future = []

    def back(self, steps: int) -> str:
        size = len(self.prev) - 1
        for _ in range(min(steps, size)):
            self.future.append(self.prev.pop())
        return self.prev[-1]

    def forward(self, steps: int) -> str:
        size = len(self.future)
        for _ in range(min(steps, size)):
            self.prev.append(self.future.pop())
        return self.prev[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
