t = int(input())
x = [1, 2, 3, 4, 5, 6, 7]
for i in range(t):
    N = int(input())
    a = list(map(int, input().split()))
    rever = a[::-1]
    dupli = set(a)
    if rever == a and list(dupli) == x:
        print('yes')
    else:
        print('no')
