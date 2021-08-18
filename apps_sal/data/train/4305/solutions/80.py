def order_weight(strng):
    def sorter(num):
        return sum([int(digit) for digit in num])

    strng_nums = strng.strip().split()
    strng_nums.sort()
    strng_nums.sort(key=sorter)

    return ' '.join(strng_nums)
