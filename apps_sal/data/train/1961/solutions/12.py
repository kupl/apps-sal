class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pointer = 0

    def visit(self, url: str) -> None:
        #print(\"visiting \" + url + \": \" + str(len(self.history)) + \" pages total\")
        #print(\"before the visit: \" + str(self.history))
        if self.pointer < len(self.history) - 1:
            del self.history[self.pointer + 1:]
        self.history.append(url)
        self.pointer = len(self.history) - 1
        #print(\"after the visit: \" + str(self.history))
        #print(\"after the visit: \" + str(len(self.history)) + \" pages total, pointer = \" + str(self.pointer))

    def back(self, steps: int) -> str:
        length = min(steps, self.pointer)
        self.pointer -= length
        #print(\"moving back, pointer = \" + str(self.pointer))
        return self.history[self.pointer]

    def forward(self, steps: int) -> str:
        length = min(steps, len(self.history) - 1 - self.pointer)
        self.pointer += length
        #print(\"moving forward, pointer = \" + str(self.pointer))
        return self.history[self.pointer]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

