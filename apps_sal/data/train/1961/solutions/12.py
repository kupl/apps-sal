class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pointer = 0

    def visit(self, url: str) -> None:
        if self.pointer < len(self.history) - 1:
            del self.history[self.pointer + 1:]
        self.history.append(url)
        self.pointer = len(self.history) - 1

    def back(self, steps: int) -> str:
        length = min(steps, self.pointer)
        self.pointer -= length
        return self.history[self.pointer]

    def forward(self, steps: int) -> str:
        length = min(steps, len(self.history) - 1 - self.pointer)
        self.pointer += length
        return self.history[self.pointer]
