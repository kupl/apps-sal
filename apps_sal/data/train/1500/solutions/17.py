# cook your dish here
for _ in range(int(input())):
    maxcount,count=0,0
    s = input()
    for i in s:
        if i == '(':
            count += 1
        else:
            count -= 1
        maxcount = max(maxcount,count)
    print('('*maxcount+')'*maxcount)
