testcase = eval(input())
while(testcase):
    dosas = eval(input())
    if dosas % 2 == 0:
        print("YES")
    elif dosas % 2 == 1:
        print("NO")
    testcase -= 1
