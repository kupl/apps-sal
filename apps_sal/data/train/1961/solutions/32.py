class Node:

    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.head.next = None
        self.head.prev = None
        self.curr = self.head

    def visit(self, url: str) -> None:
        node = Node(url)
        self.curr.next = node
        node.prev = self.curr
        self.curr = node

    def back(self, steps: int) -> str:
        count = 0
        while count < steps and self.curr.prev != None:
            self.curr = self.curr.prev
            count += 1
        return self.curr.data

    def forward(self, steps: int) -> str:
        count = 0
        while count < steps and self.curr.__next__ != None:
            self.curr = self.curr.__next__
            count += 1
        return self.curr.data
