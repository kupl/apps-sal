l = [2 ** i - 1 for i in range(0, 25)]
for _ in range(int(input())):
    (x, y) = list(map(int, input().split()))
    x_l = [i for i in l if i <= x]
    y_l = [i for i in l if i <= y]
    (count_x, count_y, final_x, final_y) = (0, 0, x + 1, y + 1)
    while True:
        temp = 0
        for i in range(len(x_l) - 1, -1, -1):
            if temp + (x_l[i] + 1) <= final_x:
                temp += x_l[i] + 1
                count_x += 1
                if temp == final_x:
                    break
        break
    while True:
        temp = 0
        for i in range(len(y_l) - 1, -1, -1):
            if temp + (y_l[i] + 1) <= final_y:
                temp += y_l[i] + 1
                count_y += 1
                if temp == final_y:
                    break
        break
    if count_x == count_y:
        print(0, 0)
    elif count_x < count_y:
        print(1, count_y - count_x)
    else:
        print(2, count_x - count_y)
