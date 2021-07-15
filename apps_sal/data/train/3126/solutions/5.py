def palindrome_rearranging(s):
    odd =0
    for char in set(s):
        if s.count(char)%2 != 0:
            odd+=1
    if odd>1:
        return False
    else:
        return True
