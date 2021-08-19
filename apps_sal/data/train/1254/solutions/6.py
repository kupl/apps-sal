# cook your dish here
for _ in range(int(input())):
    n, p = map(int, input().split())
    l = list(map(int, input().split()))
    a = c = 0
    for i in l:
        if i >= int(p / 2):
            a += 1
        elif i <= int(p / 10):
            c += 1
    print('yes' if(a == 1 and c == 2) else 'no')
