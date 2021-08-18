n = int(input())
l = list(map(int, input().split()))
for i in l:
    if i == 1:
        print(3, end=' ')
        continue
    if i == 2:
        print(1, end=' ')
        continue
    s = list(bin(i)[2:])
    if s[-2] == '1':
        s[-2] = '0'
    else:
        s[-2] = '1'
    x = int(''.join(s), 2)
    print(x, end=' ')
print()
