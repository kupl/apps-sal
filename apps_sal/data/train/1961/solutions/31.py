class BrowserHistory:

    def __init__(self, homepage: str):
        self.backwardStack = [homepage]
        self.forwardStack = []

    def visit(self, url: str) -> None:
        self.backwardStack.append(url)
        self.forwardStack.clear()

    def back(self, steps: int) -> str:
        while len(self.backwardStack) >= 2 and steps > 0:
            top = self.backwardStack.pop()
            self.forwardStack.append(top)
            steps -= 1
        return self.backwardStack[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and len(self.forwardStack) > 0:
            top = self.forwardStack.pop()
            self.backwardStack.append(top)
            steps -= 1
        return self.backwardStack[-1]
