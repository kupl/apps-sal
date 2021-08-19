class BrowserHistory:

    def __init__(self, homepage: str):

        self.hashM = {}
        self.maxIndex, self.currIndex = 0, 0
        self.hashM[self.currIndex] = homepage

    def visit(self, url: str) -> None:

        self.hashM[self.currIndex + 1] = url
        self.currIndex = self.currIndex + 1
        self.maxIndex = self.currIndex
        return(url)

    def back(self, steps: int) -> str:

        if self.currIndex - steps < 0:

            self.currIndex = 0

        else:

            self.currIndex = self.currIndex - steps

        return(self.hashM[self.currIndex])

    def forward(self, steps: int) -> str:

        if self.currIndex + steps > self.maxIndex:

            self.currIndex = self.maxIndex

        else:

            self.currIndex = self.currIndex + steps

        return(self.hashM[self.currIndex])


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
