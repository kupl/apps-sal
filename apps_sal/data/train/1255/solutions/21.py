t = int(input())
for _ in range(t):
    # lol={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q'        ,'r','s','t','u','v','w','x','y','z'}
    s, k = input().split()
    k = int(k)
    n = len(s)
    x = list(set(s))
    final = ''
    for i in range(97, 123):
        if(chr(i) in x):
            if(k > 0):
                final += chr(i)
                k -= 1
            else:
                continue
        else:
            final += chr(i)
    if(len(s) <= len(final)):
        print(final[:n])
    else:
        print('NOPE')
