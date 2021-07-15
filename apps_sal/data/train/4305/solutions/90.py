def weight(s):
    return sum([int(i) for i in s])

def order_weight(strng):
    nums = strng.split()
    return ' '.join(sorted(nums, key=lambda x: (weight(x), x)))

