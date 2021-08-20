for _ in range(int(input())):
    c = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = sum(a) - max(a)
    b = sum(b) - max(b)
    if a < b:
        print('Alice')
    elif a > b:
        print('Bob')
    else:
        print('Draw')
