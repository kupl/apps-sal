# cook your dish here
for e in range(int(input())):
    s = input()
    if len(s) >= 4:
        if(s[-4::] == '1000'):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
