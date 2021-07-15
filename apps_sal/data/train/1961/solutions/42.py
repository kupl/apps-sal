class BrowserHistory:

    def __init__(self, homepage: str):
      self.history_ = [homepage]
      self.count_ = 1

    def visit(self, url: str) -> None:
      self.history_ = self.history_[:self.count_]
      self.history_.append(url)
      self.count_ += 1
        

    def back(self, steps: int) -> str:
      if steps < self.count_:
        self.count_ -= steps
        return self.history_[self.count_-1]
      else:
        self.count_ = 1
        return self.history_[self.count_-1]
        

    def forward(self, steps: int) -> str:
      if steps <= len(self.history_) - self.count_:
        self.count_ += steps
        return self.history_[self.count_ - 1]
      else:
        self.count_ = len(self.history_)
        return self.history_[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

