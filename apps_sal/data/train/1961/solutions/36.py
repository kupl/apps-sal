class Node:
    def __init__(self, url):
        self.prev = None
        self.next = None
        self.url = url


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(\"head\")
        self.tail = Node(\"tail\")
        self.current = Node(homepage)
        self.current.prev = self.head
        self.current.next = self.tail
        self.head.next = self.current
        self.tail.prev = self.current
        
        

    def visit(self, url: str) -> None:
        if self.current.next != self.tail:
            # in the middle of the history
            p = self.current.next
            prev = None
            while p and p != self.tail:
                prev = p
                if prev:
                    del(prev)
                p = p.next
        new = Node(url)
        self.current.next = new
        new.prev = self.current
        
        new.next = self.tail
        self.tail.prev = new
        self.current = self.current.next
        return
        

    def back(self, steps: int) -> str:
        while self.current.prev != self.head and steps > 0:
            self.current = self.current.prev
            steps -= 1
        return self.current.url
            

    def forward(self, steps: int) -> str:
        print(self.current.url, steps)
        while self.current.next != self.tail and steps > 0:
            self.current = self.current.next
            steps -= 1
        return self.current.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
