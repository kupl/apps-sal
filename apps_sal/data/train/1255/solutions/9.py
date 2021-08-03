for _ in range(int(input())):
    s = input().split()
    k = int(s[1])
    s = s[0]
    ll = len(s)
    if (26 - ll + k) >= ll:
        l = [0]
        for i in range(26):
            l.append(0)
        for i in s:
            l[ord(i) - 96] = 1
        a = 0
        b = 1
        for i in range(ll):
            if a < k:
                if l[b] == 1:
                    print(chr(96 + b), end="")
                    a += 1
                else:
                    print(chr(96 + b), end="")
            else:
                while b <= 26 and l[b] == 1:
                    b += 1
                print(chr(96 + b), end="")
            b += 1
    else:
        print('NOPE', end="")
    print()
