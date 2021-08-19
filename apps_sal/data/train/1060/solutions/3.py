t = int(input())
for o in range(t):
    n = int(input())
    p = str(input())
    l = list(p)
    one = l.count('1')
    zero = l.count('0')
    count = 0
    for i in range(n):
        if l[i] == '1':
            count += zero
            one -= 1
        else:
            count += one
            zero -= 1
    print(count)
