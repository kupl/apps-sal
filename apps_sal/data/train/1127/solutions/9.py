# cook your dish here
t = int(input())
for z in range(t):
    s = input().split()
    if len(s) == 1:
        x = s[0]
        print(x.capitalize())
    else:
        for i in s:
            if i != s[-1]:
                x = i.capitalize()
                print(x[0], '.', sep='', end=' ')
            else:
                print(i.capitalize())
