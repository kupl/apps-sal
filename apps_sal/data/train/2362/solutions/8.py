def main():
    q = int(input())
    for i in range(q):
        n = int(input())
        l_x = -10 ** 5
        r_x = 10 ** 5
        l_y = -10 ** 5
        r_y = 10 ** 5
        flag = True
        for i in range(n):
            x, y, f1, f2, f3, f4 = map(int, input().split())
            if flag:
                if f1 == f3 == 0:
                    if not(x >= l_x and x <= r_x):
                        flag = False
                    else:
                        l_x = x
                        r_x = x
                elif f1 == 1 and f3 == 0:
                    r_x = min(x, r_x)
                elif f1 == 0 and f3 == 1:
                    l_x = max(x, l_x)
                if f2 == f4 == 0:
                    if not(y >= l_y and y <= r_y):
                        flag = False
                    else:
                        l_y = y
                        r_y = y
                elif f2 == 1 and f4 == 0:
                    l_y = max(y, l_y)
                elif f2 == 0 and f4 == 1:
                    r_y = min(y, r_y)
                if l_x > r_x or l_y > r_y:
                    flag = False
        if flag:
            print(1, l_x, l_y)
        else:
            print(0)


main()
