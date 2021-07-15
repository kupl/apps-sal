for _ in range(int(input())):
    N = int(input())
    binstr = input()
    a = binstr.count('1')
    b = binstr.count('0')
    print(a*b)
