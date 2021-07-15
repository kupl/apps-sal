import numpy as np


class ProductOfNumbers:
    def __init__(self):
        self.current_list_of_numbers: list = []
        self.prefix = []

    def add(self, num: int) -> None:
        if len(self.current_list_of_numbers) == 0:
            self.prefix = [num]
            self.current_list_of_numbers.append(num)
        else:

            self.prefix = np.array(self.prefix) * num
            self.prefix = np.append(self.prefix, [int(num)], 0)
            self.current_list_of_numbers.append(num)

    def getProduct(self, k: int) -> int:
        return self.prefix[len(self.prefix) - k]
