class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = []
        self.urls.append(homepage)
        self.i = 0
        self.bound = 0

    def visit(self, url: str) -> None:
        self.urls.append(url)
        self.i += 1
        if self.i == len(self.urls):
            self.urls.append(url)
        else:
            self.urls[self.i] = url
        self.bound = self.i

    def back(self, steps: int) -> str:
        self.i = max(0, self.i - steps)
        return self.urls[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.bound, self.i + steps)
        return self.urls[self.i]
