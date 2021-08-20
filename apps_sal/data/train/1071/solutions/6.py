def make_31(string):
    if len(string) < 31:
        string = (31 - len(string)) * '0' + string
    return string


for _ in range(int(input())):
    (x, Q) = list(map(int, input().split()))
    b = make_31(bin(x)[2:])
    b = list(b.strip())
    for qqq in range(Q):
        query = int(input())
        if query == 1:
            p = int(input())
            print('ON' if b[31 - p] == '1' else 'OFF')
        elif query == 2:
            p = int(input())
            b[31 - p] = '1'
        elif query == 3:
            p = int(input())
            b[31 - p] = '0'
        else:
            (p, q) = list(map(int, input().split()))
            temp = b[31 - q]
            b[31 - q] = b[31 - p]
            b[31 - p] = temp
