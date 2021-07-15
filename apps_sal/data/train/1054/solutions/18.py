t = int(input())
for q in range(t):
    s = input()
    ns = ''
    
    f = 0
    if len(s)%2 == 0:
        k = len(s) // 2
    else:
        k = (len(s)//2)+1
    
    for i in range(k):
    
        if s[i] != s[len(s)-1-i] and s[i] != '.' and s[len(s)-1-i] != '.':
            f = 1
            break
        elif s[i] == '.':
            if s[i] == s[len(s)-1-i]:
                ns += 'a'
            else:
                ns += s[len(s)-1-i]
        elif s[len(s)-1-i] == '.':
            if s[i] == s[len(s)-1-i]:
                ns += 'a'
            else:
                ns += s[i]
        else:
            ns += s[i]
    
    
    if f == 1:
        print(-1)
    elif len(s)%2 == 0:
        print(ns + ns[::-1])
    else:
        print(ns + ns[::-1][1:])
