def house_numbers_sum(inp):
    ans = 0
    for i in inp:
        ans += i
        if i == 0:
            break
    return ans
