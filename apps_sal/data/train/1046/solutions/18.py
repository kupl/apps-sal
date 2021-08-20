for _ in range(int(input())):
    (a, b) = list(map(int, input().split()))
    l = b1 = 0
    for i in range(1, 1000, 2):
        l += i
        if l > a:
            print('Bob')
            break
        b1 = b1 + i + 1
        if b1 > b:
            print('Limak')
            break
