def palindrome(num,s):
    if not (type(num) == type(s) == int) or num < 0 or s < 0:
        return "Not valid"
    
    ans, num = [], max(num, 11)
    while len(ans) != s:
        if num == int(str(num)[::-1]):
            ans.append(num)
        num += 1
    return ans
