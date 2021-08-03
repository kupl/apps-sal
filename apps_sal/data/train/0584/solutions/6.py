for i in range(int(input())):
    s = input()
    if s.count(s[0]) == len(s):
        print("0")
        continue
    if s[0] == "0":
        print("0")
        continue
    tmp = s.index("0")
    c = 1
    for j in range(tmp + 1, len(s)):
        if s[j] == "0":
            c += 1
        else:
            break
    print(c)
