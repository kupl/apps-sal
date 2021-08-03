a = eval(input())
for i in range(a):
    n = eval(input())
    count = 1
    element = 0
    flag = 0
    while n >= count:
        flag += 1
        n -= count

        element += count
        count += 1

    print(flag)
