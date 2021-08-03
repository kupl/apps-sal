# cook your dish here
for _ in range(int(input())):
    s = input()
    flag = 0
    if len(s) < 9:
        flag = 1
    else:
        if s.count('L') < 2 or s.count('T') < 2 or s.count('I') < 2 or s.count('M') < 2:
            flag = 1
    if ((s.count('E') == 1 and len(s) == 9) or (s.count('E') >= 2)) and flag != 1:
        flag = 0
    else:
        flag = 1
    if flag == 1:
        print("NO")
    else:
        print("YES")
