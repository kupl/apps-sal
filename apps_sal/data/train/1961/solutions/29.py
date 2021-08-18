class BrowserHistory:

    def __init__(self, homepage: str):
        self.before = [homepage]
        self.after = []

    def visit(self, url: str) -> None:
        self.before.append(url)
        self.after = []

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.before) > 1:
            self.after.append(self.before[-1])
            self.before.pop()
            steps -= 1
        return self.before[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and self.after:
            self.before.append(self.after[-1])
            self.after.pop()
            steps -= 1
        return self.before[-1]
