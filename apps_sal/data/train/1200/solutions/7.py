t = int(input())
for i in range(t):
    s = input()
    x = 0
    y = 2
    count = 0
    for i in range(len(s) // 2):
        a = s[x:y]
        if "A" in a and "B" in a:
            count = count + 1
        else:
            count = count
        x = x + 2
        y = y + 2
    if count == len(s) // 2:
        print("yes")
    else:
        print("no")
