from collections import deque


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = deque()
        self.future = deque()
        self.history.append(homepage)

    def visit(self, url: str) -> None:
        self.history.append(url)
        if self.future:
            self.future = deque()

    def back(self, steps: int) -> str:
        for i in range(steps):
            if len(self.history) > 1:
                self.future.append(self.history.pop())
        return self.history[-1]

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.future:
                self.history.append(self.future.pop())
        return self.history[-1]
