def uni_total(string):
    # your code here
    if string == '':
        return 0
    else:
        ans = 0
        for i in string:
            ans = ans + ord(i)
        return ans
