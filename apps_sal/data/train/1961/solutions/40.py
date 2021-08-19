class BrowserHistory:

    def __init__(self, homepage: str):
        self.back_stack = []
        self.front_stack = []
        self.curr = homepage

    def visit(self, url: str) -> None:
        self.front_stack = []
        self.back_stack.append(self.curr)
        self.curr = url

    def back(self, steps: int) -> str:
        for i in range(steps):
            if len(self.back_stack) == 0:
                return self.curr
            ans = self.back_stack.pop()
            self.front_stack.append(self.curr)
            self.curr = ans
        return ans

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if len(self.front_stack) == 0:
                return self.curr
            ans = self.front_stack.pop()
            self.back_stack.append(self.curr)
            self.curr = ans
        return ans


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
