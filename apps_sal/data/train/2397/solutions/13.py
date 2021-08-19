import math
t = int(input())


def convert(s):

    # initialization of string to ""
    new = ""

    # traverse in the string
    for x in s:
        new += x

    # return string
    return new


for i in range(t):
    a, b = list(map(int, input().split()))
    removed = []
    for j in range(a):
        removed.append(int(input(), 2))
    removed.sort()
    pointer = 0
    leftcount = 0
    for j in range(2**(b - 1) - 101, 2**(b - 1) + 101):
        if pointer < a:
            while removed[pointer] < j:
                pointer += 1
                leftcount += 1
                if pointer == a:
                    break
        if j + 1 - leftcount >= 2**b - j - 1 - (a - leftcount):
            if j in removed:
                continue
            s = "{0:b}".format(j)
            ans = []
            for k in range(b - len(s)):
                ans.append('0')
            for k in range(len(s)):
                ans.append(s[k])
            print(convert(ans))
            break
