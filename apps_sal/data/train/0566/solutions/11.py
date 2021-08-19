# cook your dish here
t = int(input())
for ts in range(t):
    s1 = str(input())
    s2 = str(input())
    c = 0
    for i in s1:
        for j in s2:
            if(i == j):
                c = c + 1
    if(c > 0):
        print('Yes')
    else:
        print('No')
