class BrowserHistory:

    def __init__(self, homepage: str):
        self.list1 = [homepage]
        self.currentInd = 0

    def visit(self, url: str) -> None:
        newList = self.list1[0:self.currentInd + 1]
        newList.append(url)
        self.currentInd += 1
        self.list1 = newList
        print((self.list1, self.currentInd))

    def back(self, steps: int) -> str:
        while self.currentInd > 0 and steps > 0:
            self.currentInd -= 1
            steps -= 1
        return self.list1[self.currentInd]

    def forward(self, steps: int) -> str:
        while self.currentInd < len(self.list1) - 1 and steps > 0:
            self.currentInd += 1
            steps -= 1
        print((self.list1[self.currentInd], self.currentInd))
        return self.list1[self.currentInd]
