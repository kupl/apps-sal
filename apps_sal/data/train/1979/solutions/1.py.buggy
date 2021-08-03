class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:

        def checkT(x):
            for n in range(x,-1,-1):
                if n in self.t:
                    self.ans += str(n)
                    self.t.remove(n)
                    return(True)
            return(False)

        for x in range(2,-1,-1):
            self.t = list(A)
            self.ans = \"\"
            if x == 2:
                if x in self.t:
                    self.ans += \"2\"
                    self.t.remove(2)
                    if checkT(3):
                        self.ans += \":\"
                        if checkT(5):
                            self.ans += str(self.t[0])
                            return(self.ans)
                continue

            if x in self.t:
                self.ans += str(x)
                self.t.remove(x)
                if checkT(9):
                    self.ans += \":\"
                    if checkT(5):
                        self.ans += str(self.t[0])
                        return(self.ans)
        return(\"\")

