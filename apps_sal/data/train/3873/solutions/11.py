
import numpy as np


def product_sans_n(nums):
    numLen = len(nums)
    leftProducts = [None for _ in range(numLen)]
    rightProducts = [None for _ in range(numLen)]
    leftRunningProduct = 1
    rightRunningProduct = 1
    for i in range(numLen):
        leftRunningProduct = leftRunningProduct * nums[i]
        leftProducts[i] = leftRunningProduct
        rightRunningProduct = rightRunningProduct * nums[numLen - 1 - i]
        rightProducts[numLen - 1 - i] = rightRunningProduct

    result = [None for _ in range(numLen)]
    for i in range(numLen):
        product = 1
        if i > 0:
            product = product * leftProducts[i - 1]
        if i < numLen - 1:
            product = product * rightProducts[i + 1]
        result[i] = product
    return result
