try:
    for z in range(int(input())):
        n = int(input())
        H = [int(e) for e in input().split()]
        if n % 2 == 0:
            print('no')
        elif H[0] != 1:
            print('no')
        else:
            f = 0
            for i in range(n // 2):
                if H[i] != H[n - i - 1]:
                    f = 1
                    break
            if f == 0:
                for i in range(n // 2):
                    if H[i] - H[i + 1] != -1:
                        f = 1
                        break
            if f == 1:
                print('no')
            else:
                print('yes')
except:
    pass
