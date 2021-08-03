def is_happy(n):
    if n == 1:
        return True
    nums = []
    while n != 1:
        if n in nums:
            return False
        nums.append(n)
        n = sum(int(x)**2 for x in list(str(n)))
        if n == 1:
            return True
