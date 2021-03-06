class BiLinkedNode:

    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.currPage = BiLinkedNode(homepage)
        self.browseListLen = 1
        self.currPageIdx = 0

    def visit(self, url: str) -> None:
        newPage = BiLinkedNode(url)
        newPage.prev = self.currPage
        self.currPage.next = newPage
        self.currPage = newPage
        self.currPageIdx += 1
        self.browseListLen = self.currPageIdx + 1

    def back(self, steps: int) -> str:
        while self.currPageIdx > 0 and steps > 0:
            self.currPage = self.currPage.prev
            self.currPageIdx -= 1
            steps -= 1
        return self.currPage.val

    def forward(self, steps: int) -> str:
        while self.currPageIdx < self.browseListLen - 1 and steps > 0:
            self.currPage = self.currPage.__next__
            self.currPageIdx += 1
            steps -= 1
        return self.currPage.val
