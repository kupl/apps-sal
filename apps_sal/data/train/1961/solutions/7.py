class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.pages = self.pages[:self.curr + 1]
        self.pages.append(url)
        self.curr = len(self.pages) - 1
        print(self.pages)

    def back(self, steps: int) -> str:
        if self.curr - steps < 0:
            self.curr = 0
            return self.pages[0]
        else:
            self.curr = self.curr - steps
            return self.pages[self.curr]

    def forward(self, steps: int) -> str:
        if self.curr + steps >= len(self.pages):
            self.curr = len(self.pages) - 1
            return self.pages[-1]
        else:
            self.curr = self.curr + steps
            return self.pages[self.curr]
