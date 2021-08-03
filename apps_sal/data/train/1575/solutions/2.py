for tt in range(eval(input())):
    m = eval(input())
    n = eval(input())
    o = eval(input())
    if m == 1 and n == 1 and o == 1:
        print('0')
        continue
    if m != 1 and n != 1 and o != 1:
        ans = abs(4 * (m - 2) + 4 * (n - 2) + 4 * (o - 2))
        print(ans)
    elif (m == 1 and n > 1 and o > 1):
        ans = (n * o) - ((2 * n) + 2 * (o - 2))
        print(ans)
    elif (n == 1 and m > 1 and o > 1):
        ans = (m * o) - ((2 * m) + 2 * (o - 2))
        print(ans)
    elif (o == 1 and m > 1 and n > 1):
        ans = (m * n) - ((2 * m) + 2 * (n - 2))
        print(ans)
