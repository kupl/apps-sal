t = int(input())
for _ in range(t):
    s = input()
    count = 0
    l = []
    for i in range(0, len(s)):
        if s[i] == ">":

            if len(l) != 0 and l[-1] == "<":
                l.pop()
                if len(l) == 0:
                    count = i + 1
            else:
                break

        else:
            l.append("<")
    print(count)
