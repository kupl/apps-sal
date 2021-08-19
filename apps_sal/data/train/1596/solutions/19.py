test_cases = int(input())
for i in range(test_cases):
    (X, Y) = map(int, input().split())
    X += 1
    Y += 1
    x = str(bin(X))
    y = str(bin(Y))
    count1 = 0
    count2 = 0
    for i in x:
        if i == '1':
            count1 += 1
    for i in y:
        if i == '1':
            count2 += 1
    if count1 > count2:
        print(2, abs(count1 - count2))
    elif count2 > count1:
        print(1, abs(count1 - count2))
    else:
        print(0, 0)
