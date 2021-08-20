class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.cur = 0
        self.f = 0

    def visit(self, url: str) -> None:
        self.arr = self.arr[:self.cur + 1]
        self.arr.append(url)
        self.cur += 1
        self.f = 0

    def back(self, steps: int) -> str:
        if steps > self.cur:
            self.cur = 0
            self.f = len(self.arr) - 1
        else:
            self.cur -= steps
            self.f += steps
        return self.arr[self.cur]

    def forward(self, steps: int) -> str:
        if steps > self.f:
            self.cur = len(self.arr) - 1
            self.f = 0
        else:
            self.cur += steps
            self.f -= steps
        return self.arr[self.cur]
