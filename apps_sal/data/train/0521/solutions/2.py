# f = open("file.txt", 'r+')
# inp = f.readline
import math
inp = input


for _ in range(int(input())):

    n = int(input())
    arr = list(map(int, input().split()))
    p, q = map(int, input().split())

    ans = 0
    arr.sort()

    for i in range(n // 2):

        mn, mx = arr[i], arr[n - i - 1]

        if(mx == p) or (mn == p):
            #         print("Case 1")
            adj = q
            opp = mx - mn
            val = math.atan2(opp, adj)
        elif(mn < p) and (mx > p):
            #         print("Case 2")
            adj = q
            opp = p - mn
            valA = math.atan2(opp, adj)

            opp = mx - p
            valB = math.atan2(opp, adj)

            val = valA + valB
        else:
            #         print("Case 3")
            if(p < mn):
                adj = abs(mx - p)
                opp = q
                valA = math.atan2(opp, adj)

                adj = abs(mn - p)
                valB = math.atan2(opp, adj)

                val = valA - valB
            else:
                adj = abs(p - mn)
                opp = q
                valA = math.atan2(opp, adj)

                adj = abs(p - mx)
                valB = math.atan2(opp, adj)

                val = valA - valB
        val = abs(val)

        ans += val
#     val = print('%.2f'%val)
    print('%.12f' % ans)
