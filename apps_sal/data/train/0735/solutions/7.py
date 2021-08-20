testcase = eval(input())
while testcase:
    dosas = eval(input())
    x = dosas % 10
    if x == 0 or x == 2 or x == 4 or (x == 6) or (x == 8):
        print('YES')
    else:
        print('NO')
    testcase -= 1
