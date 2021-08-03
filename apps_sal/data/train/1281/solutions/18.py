t = int(input())
for i in range(t):
    l = int(input())
    li = list(map(int, input().split()))[:l]
    a = []
    b = [1, 2, 3, 4, 5, 6, 7]
    for i in li:
        if i not in a:
            a.append(i)
    a.sort()
    if a == b and li == li[::-1]:
        print('yes')
    else:
        print('no')
