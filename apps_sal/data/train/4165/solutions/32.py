def uni_total(string):
    ans = 0
    if string:    
        for _ in string:
            ans += ord(_)
    return ans
