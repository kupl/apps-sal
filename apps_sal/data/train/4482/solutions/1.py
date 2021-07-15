def even_numbers_before_fixed(sequence, fixed_element):
    ans = 0
    for s in sequence:
        if s == fixed_element:
            return ans
        ans += (s % 2 == 0)
    return -1
