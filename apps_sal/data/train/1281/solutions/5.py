x = [1, 2, 3, 4, 5, 6, 7]
for i in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    revli = li[::-1]
    dupli = set(li)
    if li == revli and list(dupli) == x:
        print('yes')
    else:
        print('no')
