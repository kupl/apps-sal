tc = int(input())
for i in range(tc):
    input()
    ls = list(map(int, input().split(' ')))
    p = 'YES'
    for i in range(1, len(ls) + 1):
        if -1 > i - ls[i - 1] or i - ls[i - 1] > 1:
            p = 'NO'
            break
    print(p)
