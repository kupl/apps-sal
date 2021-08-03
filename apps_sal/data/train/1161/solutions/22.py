# cook your dish here
for _ in range(int(input())):
    s = list(input())
    c = 0
    for i in range(len(s)):
        if s[i] == 'm' and i > 0 and s[i - 1] == "s":
            s[i - 1] = ""
        elif s[i] == 'm' and i < len(s) - 1 and s[i + 1] == "s":
            s[i + 1] = ""
    sc = s.count('s')
    mc = s.count('m')
    if sc > mc:
        print('snakes')
    elif mc > sc:
        print('mongooses')
    else:
        print('tie')
