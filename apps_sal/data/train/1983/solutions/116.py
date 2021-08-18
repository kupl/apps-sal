class ProductOfNumbers:

    def __init__(self):
        self.__list = []
        self.__product = []

    def add(self, num: int) -> None:
        self.__list.append(num)
        if num == 0:
            self.__product = []
        else:
            if not self.__product:
                self.__product = [1]

            self.__product.insert(0, self.__product[0] * num)

    def getProduct(self, k: int) -> int:
        p = self.__product
        try:
            return p[0] // p[k]
        except IndexError:
            return 0
