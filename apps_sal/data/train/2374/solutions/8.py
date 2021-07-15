a = int(input())
for i in range(a):
    b = int(input())
    c = input()
    d = input()
    l = [c, d]
    k = 0
    ans = 1
    for i in range(b):
        if l[k][i] == '1' or l[k][i] == '2':
            pass
        else:
            if l[1 - k][i] == "3" or l[1 - k][i] == "4" or l[1 - k][i] == "5" or l[1 - k][i] == "6":
                k = 1 - k
            else:
                ans = 0 
    if k == 1 and ans == 1:
        print('YES')
    else:
        print('NO')
