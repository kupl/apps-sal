class Node:
    def __init__(self, url: str):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.current_node = self.head
        

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.current_node.next = new_node
        new_node.prev = self.current_node
        self.current_node = self.current_node.__next__
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.current_node == self.head:
                break
            else:
                self.current_node = self.current_node.prev
        return self.current_node.url
        
    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.current_node.__next__ is None:
                break
            else:
                self.current_node = self.current_node.__next__
        return self.current_node.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

