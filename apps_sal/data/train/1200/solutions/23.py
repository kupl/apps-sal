for _ in range(int(input())):
    s = input()
    if s.count("A") == s.count("B"):
        flag = 1
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                pass
            else:
                flag = 0
                break
        if flag == 0:
            print("no")
        else:
            print("yes")
    else:
        print("no")
