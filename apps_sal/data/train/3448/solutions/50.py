def f(n):
    try:
        val = int(n)
        if val <= 0:
            return None
    except ValueError:
        return None
    else:
        i = 0
        nums = []
        while i < n:
            if type(n) != int:
                return None
            else:
                i += 1
                nums.append(i)
        return sum(nums)
