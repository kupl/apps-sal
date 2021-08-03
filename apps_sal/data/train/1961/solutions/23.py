class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = ListNode(homepage)

    def visit(self, url: str) -> None:

        node = ListNode(url)
        node.prev = self.root
        self.root.next = node
        self.root = self.root.__next__

    def back(self, steps: int) -> str:
        while self.root.prev and steps:
            self.root = self.root.prev
            steps -= 1

        return self.root.val

    def forward(self, steps: int) -> str:
        while self.root.__next__ and steps:
            self.root = self.root.__next__
            steps -= 1
        return self.root.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
