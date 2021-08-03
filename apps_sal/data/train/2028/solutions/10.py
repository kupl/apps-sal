def isPalindrome(s):
    return s == s[::-1]


s = input()
r = 0
for i in set(s):
    r = max(r, s.count(i))
# print(r)
if len(set(s)) == 1 or len(s) <= 3:
    print("Impossible")
elif r >= len(s) - 1:
    print("Impossible")
else:
    fl = 0
    for i in range(len(s)):
        e = s[0:i]
        f = s[i:]
        e = f + e
        # print(e)
        # fl=0
        if isPalindrome(e) and e != s:
            fl = 1
            print(1)
            break
    if fl == 0:
        print(2)
