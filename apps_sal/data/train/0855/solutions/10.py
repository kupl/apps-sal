t = input()
t = int(t)
while(t > 0):
    s = input()
    for i in range(len(s) - 1, -1, -1):
        print(s[i], end="")
    t -= 1
