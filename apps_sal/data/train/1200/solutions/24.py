def string(s):
    x = 0
    for i in range(0, len(s) - 1, +2):
        if s[i] == s[i + 1]:
            x = 0
            return "no"
        else:
            x = 1
    if x == 1:
        return "yes"


for _ in range(int(input())):
    s = input()
    print(string(s))
