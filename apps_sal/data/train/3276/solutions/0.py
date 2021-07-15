def missing(nums, s):
    ans = []
    s = s.replace(' ','')
    try:
        for i in sorted(nums):
            ans.append(s[i])
        return ''.join(ans).lower()
    except IndexError:
        return ("No mission today")
