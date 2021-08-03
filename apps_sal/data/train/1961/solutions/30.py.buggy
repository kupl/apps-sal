class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr_page = homepage
        self.prev_pages = []
        self.next_pages = []

    def __str__(self):
        return \"{0}-{1}-{2}\".format(self.prev_pages, self.curr_page, self.next_pages[::-1])
        
    def visit(self, url: str) -> None:
        self.prev_pages.append(self.curr_page)
        self.curr_page = url
        self.next_pages = []

    def back(self, steps: int) -> str:
        counter = min(steps, len(self.prev_pages))
    
        while counter > 0:
            self.next_pages.append(self.curr_page)
            self.curr_page = self.prev_pages.pop(-1)
            counter -= 1
        return self.curr_page
        
    def forward(self, steps: int) -> str:
        counter = min(steps, len(self.next_pages))
        
        while counter > 0:
            self.prev_pages.append(self.curr_page)
            self.curr_page = self.next_pages.pop(-1)
            counter -= 1
        return self.curr_page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
