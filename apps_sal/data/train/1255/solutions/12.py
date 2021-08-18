for t in range(int(input())):
    flag = False
    a = [0] * 26
    s, k = (input().split())
    k = int(k)
    s = list(s)
    n = len(s)
    nn = n
    ans = []
    for i in range(n):
        a[ord(s[i]) - ord('a')] = 1
    for i in range(26):
        if(a[i] == 0 and n > 0):
            flag = True

            ans.append(chr(ord('a') + i))
            n -= 1
        elif (a[i] == 1 and n > 0 and k > 0):
            ans.append(chr(ord('a') + i))
            n -= 1
            k -= 1
            flag = True
    if(flag and len(ans) == nn):
        for i in ans:
            print(i, end='')
        print()
    else:
        print("NOPE")
