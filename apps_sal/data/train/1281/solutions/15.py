# cook your dish here
t = int(input())
for i in range(t):
    l = int(input())
    li = list(map(int, input().split()))[:l]
    a1 = []
    a2 = [1, 2, 3, 4, 5, 6, 7]
    a3 = li[::-1]
    for i in li:
        if i not in a1:
            a1.append(i)
    a1.sort()
    if a1 == a2 and li == a3:
        print('yes')
    else:
        print('no')
