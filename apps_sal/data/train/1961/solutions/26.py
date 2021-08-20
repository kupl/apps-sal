class BrowserHistory:

    def __init__(self, homepage: str):
        self.forwardA = []
        self.backward = [homepage]

    def visit(self, url: str) -> None:
        self.backward.append(url)
        self.forwardA = []

    def forward(self, steps: int) -> str:
        i = 0
        while len(self.forwardA) != 0 and i < steps:
            i += 1
            item = self.forwardA.pop()
            self.backward.append(item)
        return self.backward[-1]

    def back(self, steps: int) -> str:
        i = 0
        while len(self.backward) > 1 and i < steps:
            item = self.backward.pop()
            self.forwardA.append(item)
            i += 1
        return self.backward[-1]
