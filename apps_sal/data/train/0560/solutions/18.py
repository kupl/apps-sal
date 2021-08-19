for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum(a) - max(a) < sum(b) - max(b):
        print('Alice')
    elif sum(a) - max(a) == sum(b) - max(b):
        print('Draw')
    else:
        print('Bob')
