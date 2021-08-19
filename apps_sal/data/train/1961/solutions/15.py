class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = LinkedList(homepage, None, None)
        self.curr_page = self.history

    def visit(self, url: str) -> None:
        new_page = LinkedList(url, self.curr_page, None)
        self.curr_page.next = new_page
        self.curr_page = new_page

    def back(self, steps: int) -> str:
        num_steps = 0
        temp = self.curr_page
        while num_steps < steps and temp.prev != None:
            temp = temp.prev
            num_steps += 1
        self.curr_page = temp
        return temp.val

    def forward(self, steps: int) -> str:
        num_steps = 0
        temp = self.curr_page
        while num_steps < steps and temp.__next__ != None:
            temp = temp.__next__
            num_steps += 1
        self.curr_page = temp
        return temp.val


class LinkedList:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
