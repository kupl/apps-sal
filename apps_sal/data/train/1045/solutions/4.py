l = 'aeiou'
ll = 'bcdfghjklmnpqrstvwxyz'
for u in range(int(input())):
    s = input()
    r = ''
    for i in range(len(s)):
        if(s[i] in l):
            r = r + '0'
        elif(s[i] in ll):
            r = r + '1'
    b = int(r, 2)
    print(b % (1000000007))
