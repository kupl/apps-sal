# cook your dish here
for i in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    a = sum(l1) - max(l1)
    b = sum(l2) - max(l2)
    if a > b:
        print('Bob')
    elif b > a:
        print('Alice')
    else:
        print('Draw')
