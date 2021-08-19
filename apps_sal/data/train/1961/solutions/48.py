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
        # print(\"back\")
        for i in range(steps):
            if len(self.history) > 1:
                self.future.append(self.history.pop())
        # print(self.history,self.future )
        return self.history[-1]

    def forward(self, steps: int) -> str:
        # print(\"forward\")
        for i in range(steps):
            if self.future:
                self.history.append(self.future.pop())
        # print(self.history,self.future)
        return self.history[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
