class BrowserHistory:
    curr = 0
    history = []

    def __init__(self, homepage: str):
        self.curr = 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.curr += 1
        print(self.history)
        self.history = self.history[0:self.curr]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, len(self.history) - 1)
        return self.history[self.curr]
