class Node:
    
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class BrowserHistory(object):

    def __init__(self, homepage):
        \"\"\"
        :type homepage: str
        \"\"\"
        self.head = Node(val=homepage)

    def visit(self, url):
        \"\"\"
        :type url: str
        :rtype: None
        \"\"\"
        self.head.next = Node(val=url, prev=self.head)
        self.head = self.head.next

    def back(self, steps):
        \"\"\"
        :type steps: int
        :rtype: str
        \"\"\"
        while steps and self.head.prev:
            self.head = self.head.prev
            steps -= 1
        return self.head.val
        

    def forward(self, steps):
        \"\"\"
        :type steps: int
        :rtype: str
        \"\"\"
        while steps and self.head.next:
            self.head = self.head.next
            steps -= 1
        return self.head.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
