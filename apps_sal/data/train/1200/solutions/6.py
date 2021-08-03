for _ in range(int(input())):
    s = input()
    if len(s) & 1 == 1:
        print("no")
    else:
        for i in range(0, len(s), 2):
            x = s[i:i + 2]
            if x == "AA" or x == "BB":
                print("no")
                break
        else:
            print("yes")
