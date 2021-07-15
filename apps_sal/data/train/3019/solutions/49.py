def str_count(strng, letter):
    ans = 0
    for c in strng:
        if c == letter:
            ans += 1
    return ans
