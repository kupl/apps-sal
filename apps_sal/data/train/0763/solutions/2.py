t = int(input())
for _ in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    rem = 0
    if (s1.count('1') == s2.count('1') and s1.count('0') == s2.count('0')):
        u1 = 0
        n1 = 0
        s1 = list(s1)
        s2 = list(s2)
        for i in range(n):
            if s1[i] != s2[i]:
                if s1[i] == '1':
                    u1 += 1
                elif s2[i] == '1':
                    n1 += 1
                if u1 < n1:
                    rem = 1
                    break
        if rem == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
