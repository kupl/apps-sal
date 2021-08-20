class ProductOfNumbers:

    def __init__(self):
        self.a = []

    def add(self, num: int) -> None:
        x = [0] * 101
        x[num] += 1
        if len(self.a) > 0:
            for i in range(101):
                x[i] += self.a[-1][i]
        self.a.append(x)

    def getProduct(self, k: int) -> int:
        res = 1
        for i in range(101):
            cnt = self.a[-1][i]
            if len(self.a) > k:
                cnt -= self.a[-(k + 1)][i]
            res *= pow(i, cnt)
        return res
