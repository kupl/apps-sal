# cook your dish here
# cook your dish here
x = int(input())
for i in range(x):
    y = int(input())
    lst = list(map(int, input().split()))
    c = []
    for j in lst:
        if j not in c:
            c.append(j)
    c.sort()
    print('yes' if (c == [1, 2, 3, 4, 5, 6, 7] and lst == lst[::-1]) else 'no')
