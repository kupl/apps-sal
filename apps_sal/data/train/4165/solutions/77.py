def uni_total(string):
    #your code here
    ans = 0
    for i in range(len(string)):
        ans += ord(string[i])
    return ans
