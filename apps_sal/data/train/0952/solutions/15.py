# cook your dish here
try:
    t = int(input())
    while t > 0:
        t -= 1
        su = 0
        s = input()
        a = ["a", "e", "i", "o", "u"]

        for i in range(len(s)):
            if s[i].isalpha():
                if s[i] in a:
                    continue
                minn = 26
                for j in range(5):
                    tem = abs(ord(a[j]) - ord(s[i]))

                    if tem < minn:
                        minn = tem

                su += minn

        print(su)
except:
    pass
