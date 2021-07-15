# n = int(input())

# while n > 0:

#     t = int(input())

#     total = 0

#     arr = list(map(int, input().split()))

#     for i in arr:

#         if i == 5:
#             total += 5
#         else:
#             total -= (i-5)
            
#             if total != 0:
#                 print("NO")
#                 break
#     else:
#         print("YES")
#     n-=1

n = int(input())

while n > 0:

    t = int(input())
    d = {5: 0, 10:0, 15:0}

    arr = list(map(int, input().split()))

    for temp in arr:

        if d[5] < 0:
            print("NO")
            break

        if temp == 5:
            d[temp] += 1

        elif temp == 10:
            if d[5] >= 1:
                d[10] += 1
                d[5] -= 1
            else:
                print("NO")
                break

        elif temp == 15:
            if d[10] >= 1:
                #d[15] += 1
                d[10] -= 1
            else:
                # print("NO")
                # break
                if d[5] >= 2:
                    d[5]-=2
                    d[15] += 1
                else:
                    print('NO')
                    break
        else:
            print("NO")
            break
    else:
        print("YES")
    n-=1
