def order_weight(strng):
    nums = sorted(sorted(strng.split(' ')), key=lambda x: sum([int(i) for i in x]))
    return " ".join(nums)
