def reverse_number(num):
    ans = int(str(num)[::-1]) if num >= 0 else -int(str(-num)[::-1])
    return ans
