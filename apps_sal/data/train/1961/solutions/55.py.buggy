\"\"\"

[\"google\", \"facebook\", \"youtube\"]
cur = 0
length = 3


[\"google\", \"linkedin\"]
cur = 1
length = 2

if cur == length - 1:
    add one more element
else:
    replace the next element

Details 
Input
[\"google\", \"linkedin\"]
cur = 1

[\"BrowserHistory\",\"visit\",     \"visit\",\"back\",\"visit\",    \"forward\",\"visit\",     \"visit\",  \"forward\",\"visit\",\"back\",\"visit\",\"visit\",\"forward\"]
[[\"esgriv.com\"],[\"cgrt.com\"],[\"tip.com\"],[9],[\"kttzxgh.com\"],[7],[\"crqje.com\"],[\"iybch.com\"],[5],   [\"uun.com\"],[10],[\"hci.com\"],[\"whula.com\"],[10]]
[null,              null,      null, \"esgriv.com\",null,  \"kttzxgh.com\",null,       null,   \"crqje.com\",null,\"esgriv.com\",null,null,\"tip.com\"]
[null,               null,     null, \"esgriv.com\",null,  \"kttzxgh.com\",null,        null,  \"iybch.com\",null,\"esgriv.com\",null,null,\"whula.com\"]
[\"esgriv.com\",\"kttgzxgh.com\", \"tip.com\"]
                 cur
                               length 

\"\"\"

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage] 
        self.cur = 0
        self.length = 1

    def visit(self, url: str) -> None:
        # append if needed
        self.cur += 1
        if self.cur == len(self.history):
            self.history.append(url)
        else:
            self.history[self.cur] = url
        self.length = self.cur + 1

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]
        

    def forward(self, steps: int) -> str:
        self.cur = min(self.length - 1, self.cur + steps)
        return self.history[self.cur]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
