class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.forwardHistory = []
        self.curr = homepage

    def visit(self, url: str) -> None:
        self.history.append(self.curr)
        self.curr = url
        self.forwardHistory = []

    def back(self, steps: int) -> str:
        if not self.history:
            return self.curr
        left = steps
        url = None
        while left and self.history:
            url = self.history.pop()
            left -= 1
            self.forwardHistory.append(self.curr)
            self.curr = url
        return url

    def forward(self, steps: int) -> str:
        if not self.forwardHistory:
            return self.curr
        left = steps
        url = None
        while left and self.forwardHistory:
            url = self.forwardHistory.pop()
            left -= 1
            self.history.append(self.curr)
            self.curr = url
        return url
