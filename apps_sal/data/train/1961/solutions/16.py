class BrowserHistory:

    def __init__(self, homepage: str):
        self.pointer = 0
        self.histlen = 1
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.history = self.history[:(self.pointer + 1)] + [url]
        self.pointer += 1
        self.histlen = len(self.history)

    def back(self, steps: int) -> str:
        self.pointer = max(self.pointer - steps, 0)
        return self.history[self.pointer]

    def forward(self, steps: int) -> str:
        self.pointer = min(self.pointer + steps, self.histlen - 1)
        return self.history[self.pointer]
