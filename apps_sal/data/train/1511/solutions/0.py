# cook your dish here
# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    # reading the string
    s = input()
    i, j = 0, 0
    q = 0
    while(i < n and j < n):
        if(s[i] == 'M'):
            if(s[j] == 'I'):
                cnt = 0
                if(i > j):
                    p = s[j:i]
                    cnt = p.count(':')
                else:
                    p = s[i:j]
                    cnt = p.count(':')
                t = k + 1 - abs(i - j) - cnt
                if(t > 0):
                    q += 1
                    i += 1
                    j += 1
                else:
                    if(i < j):
                        i += 1
                    else:
                        j += 1
            elif(s[j] == 'X'):
                j += 1
                i = j
            else:
                j += 1
        elif(s[i] == 'X'):
            i += 1
            j = i
        else:
            i += 1
    print(q)
