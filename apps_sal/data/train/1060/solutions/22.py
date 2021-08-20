n = int(input())
while n > 0:
    l = int(input())
    s = input()
    zero = 0
    one = 0
    subs = 0
    for i in range(l):
        if s[i] == '0':
            zero += 1
        else:
            one += 1
    subs = one * zero
    print(subs)
    n -= 1
