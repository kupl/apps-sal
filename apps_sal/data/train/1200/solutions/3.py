T = int(input())
for i in range(0, T):
    s = input()
    x = True
    for j in range(0, len(s) - 1, 2):
        if (s[j] == "A" and s[j + 1] == "B") or (s[j] == "B" and s[j + 1] == "A"):
            continue

        else:
            x = False
            break
    if x == True:
        print("yes")
    else:
        print("no")
