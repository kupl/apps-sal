x = int(input())
lst = [1, 2, 5, 10, 50, 100]
for i in range(x):
    y = int(input())
    c = 5
    a = 0
    while(y > 0):
        if(y >= lst[c]):
            y = y - lst[c]
            a = a + 1
        else:
            c = c - 1
    print(a)
