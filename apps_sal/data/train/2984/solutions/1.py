def infected_zeroes(lst):
    left, *enclosed, right = "".join(str(digit) for digit in lst).split("0")
    return max(len(left), len(right), *((len(ones) + 1)//2 for ones in enclosed))
