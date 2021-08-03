for u in range(int(input())):
    s = input()
    i = 0
    j = len(s) - 1
    c = 1
    m = 10**7 + 9
    while(i <= j):
        if(s[i] == s[j] == '?'):
            c = ((26 % m) * (c % m)) % m
            i += 1
            j -= 1
        elif(s[i] == '?' or s[j] == '?' or s[i] == s[j]):
            i += 1
            j -= 1
        else:
            c = 0
            break
    print(c % m)
