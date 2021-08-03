# cook your dish here
for i in range(int(input())):
    s1 = input()
    s2 = input()
    c = 0
    for i in s1:
        for j in s2:
            if(i == j):
                c += 1
    if(c > 0):
        print('Yes')
    else:
        print('No')
