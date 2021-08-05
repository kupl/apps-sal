for t in range(int(input())):
    s = input()
    x = s.count('m')
    y = s.count('s')
    i = 0
    while i < len(s) - 1:
        if (s[i] == 'm' and s[i + 1] == 's') or (s[i] == 's' and s[i + 1] == 'm'):
            y = y - 1
            i = i + 2
        else:
            i = i + 1
    if x > y:
        print("mongooses")
    elif y > x:
        print("snakes")
    else:
        print("tie")
