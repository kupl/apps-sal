class BrowserHistory:

    def __init__(self, homepage: str):
        self.l = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        if self.curr == len(self.l) - 1:
            self.l.append(url)
            self.curr += 1
        else:
            while self.curr < len(self.l) - 1:
                self.l.pop()
            self.l.append(url)
            self.curr += 1

    def back(self, steps: int) -> str:
        if self.curr - steps < 0:
            self.curr = 0
            return self.l[0]
        self.curr -= steps
        return self.l[self.curr]

    def forward(self, steps: int) -> str:
        if self.curr + steps >= len(self.l):
            self.curr = len(self.l) - 1
            return self.l[-1]
        self.curr += steps
        return self.l[self.curr]
