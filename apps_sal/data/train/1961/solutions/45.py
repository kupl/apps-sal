class BrowserHistory:

    def __init__(self, homepage: str):
        self.ls=[homepage]
        self.cur=0

    def visit(self, url: str) -> None:
        last=len(self.ls)-1
        while last!=self.cur:
            self.ls.pop()
            last-=1
        self.ls.append(url)
        self.cur=len(self.ls)-1

    def back(self, steps: int) -> str:
        while steps!=0 and self.cur>0:
            self.cur-=1
            steps-=1
        return self.ls[self.cur]

    def forward(self, steps: int) -> str:
        while steps!=0 and self.cur<len(self.ls)-1:
            self.cur+=1
            steps-=1
        return self.ls[self.cur]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

