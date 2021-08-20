class BrowserHistory:

    def __init__(self, homepage: str):
        self.ls = []
        self.ls.append(homepage)
        self.hm = {}
        self.cur = 0

    def visit(self, url: str) -> None:
        self.ls = self.ls[:self.cur + 1]
        self.ls.append(url)
        self.cur = len(self.ls) - 1

    def back(self, steps: int) -> str:
        if steps > self.cur:
            self.cur = 0
            return self.ls[0]
        self.cur -= steps
        return self.ls[self.cur]

    def forward(self, steps: int) -> str:
        if steps > len(self.ls) - self.cur - 1:
            self.cur = len(self.ls) - 1
            return self.ls[self.cur]
        self.cur += steps
        return self.ls[self.cur]
