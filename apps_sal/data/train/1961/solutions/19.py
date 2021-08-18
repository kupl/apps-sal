class BrowserHistory:

    def __init__(self, homepage: str):
        self.list = []
        self.list.append(homepage)
        self.currentIndex = 0

    def visit(self, url: str) -> None:
        self.currentIndex += 1
        while self.currentIndex < len(self.list):
            self.list.pop()

        self.list.append(url)

    def forward(self, steps: int) -> str:
        self.currentIndex = min(self.currentIndex + steps, len(self.list) - 1)
        return self.list[self.currentIndex]

    def back(self, steps: int) -> str:
        self.currentIndex = max(self.currentIndex - steps, 0)
        return self.list[self.currentIndex]
