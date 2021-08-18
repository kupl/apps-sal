class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current + 1]
        self.history.append(url)
        self.current = len(self.history) - 1

    def back(self, steps: int) -> str:
        ex = max(self.current - steps, 0)
        self.current = ex
        return self.history[ex]

    def forward(self, steps: int) -> str:
        if self.current + steps < len(self.history) - 1:
            self.current += steps
        else:
            self.current = len(self.history) - 1
        return self.history[self.current]
