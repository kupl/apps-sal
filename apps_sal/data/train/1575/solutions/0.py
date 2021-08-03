for _ in range(int(input())):
    m = int(input())
    n = int(input())
    o = int(input())
    ans = 4 * (m + n + o) - 24
    if(ans <= 0):
        print('0')
    else:
        print(ans)
