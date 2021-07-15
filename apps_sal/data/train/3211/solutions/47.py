def divide(weight):
    nums = range(2, weight, 2)
    for a in nums:
        for b in nums:
            if weight == a + b:
                return True
    return False
