# cook your dish here
for _ in range(int(input())):
    s = input()
    maxcount = 0
    count = 0
    for i in s:
        if i == '(':
            count += 1
        else:
            count -= 1
        maxcount = max(maxcount, count)
    print('(' * maxcount + ')' * maxcount)
