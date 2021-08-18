class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = homepage
        self.history = [homepage] + [0 for _ in range(5000)]
        self.curr_ind = 0
        self.top = 0

    def visit(self, url: str) -> None:
        self.history[self.curr_ind + 1] = url
        self.curr_ind += 1
        self.top = self.curr_ind

    def back(self, steps: int) -> str:

        self.curr_ind = max(0, self.curr_ind - steps)
        return self.history[self.curr_ind]

    def forward(self, steps: int) -> str:

        self.curr_ind = min(self.top, self.curr_ind + steps)
        return self.history[self.curr_ind]
