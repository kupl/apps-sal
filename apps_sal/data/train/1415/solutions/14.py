# cook your dish here
t = int(input())


def fun(s):
    for i in range(len(s) - 1):
        s1 = s[:i] + s[i + 1:]
        if s1 == s1[::-1]:
            return True

    s1 = s[:len(s)]
    if s1 == s1[::-1]:
        return True
    return False


for _ in range(t):
    s = input()
    if fun(s):
        print("YES")
    else:
        print("NO")
