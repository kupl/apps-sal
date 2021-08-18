def piano(s):
    acount = s.count('A')
    bcount = s.count('B')
    if acount != bcount:
        return False
    for i in range(0, len(s) - 1, 2):
        if s[i] == s[i + 1]:
            return False
    return True


for _ in range(int(input())):
    s = list(input())
    if piano(s):
        print("yes")
    else:
        print("no")
