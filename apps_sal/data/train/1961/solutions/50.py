class BrowserHistory:
    curr = None
    backHistory = 0
    forwardHistory = 0

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        # break forward history
        self.forwardHistory = 0
        self.curr.next = Node(url)
        self.curr.next.prev = self.curr
        self.backHistory += 1
        self.curr = self.curr.__next__

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            self.forwardHistory += 1
            self.backHistory -= 1
            steps -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.__next__:
            self.curr = self.curr.__next__
            self.forwardHistory -= 1
            self.backHistory += 1
            steps -= 1
        return self.curr.url


class Node:
    url = None
    prev = None
    next = None

    def __init__(self, url: str):
        self.url = url
        self.prev = None
        self.next = None


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
