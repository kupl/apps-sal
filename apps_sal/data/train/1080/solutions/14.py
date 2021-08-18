t = int(input())
for i in range(t):
    s = input()
    l = len(s)
    l1 = l / 2
    if l % 2 == 0:
        s1 = ""
        a = s[0]
        b = s[1]
        if a != b:
            s1 += a + b
            if s.count(s1) == l1:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
