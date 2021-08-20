class ProductOfNumbers:
    from numpy import prod

    def __init__(self):
        self.numbers = []

    def add(self, num: int) -> None:
        self.numbers.append(num)

    def getProduct(self, k: int) -> int:
        return prod(self.numbers[len(self.numbers) - k:len(self.numbers)])
