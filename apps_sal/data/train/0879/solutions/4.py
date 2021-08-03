for _ in range(int(input())):
    x, y = [int(x) for x in input().split()]
    if x < y:
        print(0)
    else:
        s = 0
        for _ in range(y, x, y):
            s += (_ % 10)
        print(s)
        # team1,team2,res=[],[],0
        # for _ in range(1,x+1):
        #     if _%y==0:
        #         team1.append(_)
        #     else:
        #         team2.append(_)
        # for _ in range(len(team1)):
        #     res+=(team1[_]%10)
        # print(res)
