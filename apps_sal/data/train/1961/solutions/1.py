class BrowserHistory:

    def __init__(self, homepage: str):
        self.l = [homepage]
        self.cur = 0
        self.max = 0

    def visit(self, url: str) -> None:
        self.cur += 1
        if self.cur == len(self.l):
            self.l.append(url)
        else:
            self.l[self.cur] = url
        self.max = self.cur

    def back(self, steps: int) -> str:
        self.cur -= steps
        if self.cur < 0:
            self.cur = 0
        return self.l[self.cur]

    def forward(self, steps: int) -> str:
        self.cur += steps
        if self.cur > self.max:
            self.cur = self.max
        return self.l[self.cur]
