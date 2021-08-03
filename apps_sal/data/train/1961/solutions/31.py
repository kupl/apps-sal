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


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

#   def __init__(self, homepage: str):
#         self.back_stack = [homepage]
#         self.forward_stack = []

#     def visit(self, url: str) -> None:
#         self.forward_stack.clear()
#         self.back_stack.append(url)

#     def back(self, steps: int) -> str:
#         while len(self.back_stack) >= 2 and steps > 0:
#             top = self.back_stack.pop()
#             self.forward_stack.append(top)
#             steps -= 1
#         return self.back_stack[-1]

#     def forward(self, steps: int) -> str:
#         while len(self.forward_stack) > 0 and steps > 0:
#             top = self.forward_stack.pop()
#             self.back_stack.append(top)
#             steps -= 1
#         return self.back_stack[-1]
