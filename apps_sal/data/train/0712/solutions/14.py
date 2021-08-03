# cook your dish here


for testcase in range(int(input())):
    n = int(input())
    sol = [int(i) for i in input().split()]
    main = 1
    a = [0] * 10
    for z in sol:
        if(z % 2 == 0):
            main = 0
    if(main):
        print("YES")
    else:
        print("NO")
