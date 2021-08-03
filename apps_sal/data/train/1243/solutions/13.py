for _ in range(int(input())):
    n = int(input())
    a = str(n)
    if(a.count('0') or a.count('5')):
        print('1')
    else:
        print('0')
